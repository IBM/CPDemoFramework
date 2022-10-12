#!/bin/bash

# # source ./functions.sh

#cloud pak(s)
cpak=$1
#backup or restore operation
operation=$2

# Check if we can access the cluster
oc cluster-info
# Check if the last command executed properly
if [ $? -ne 0 ]; then
    echo "OpenShift cluster is not accessible, make sure you run the configuration steps";
    exit 1
fi

# Conditionally set the backup configuration
if [[ "${operation}" == *"backup"* ]];then
    BR_SCRIPT=pod-backup.sh                  #script to run in pod
    BR_JOB=cloud-pak-backup                  #Job name to be used
    CPD_INSTANCE=cpd-instance                #Namespace where cpd is installed
    CPD_INSTANCE_BACKUP=cpd-instance-backup  #cpd instance backup will be saved with this name
    CPD_OPERATOR_BACKUP=cpd-operator-backup  #cpd operator backup will be saved with this name
fi
# Conditionally set the restore configuration
if [[ "${operation}" == *"restore"* ]];then
    BR_SCRIPT=pod-restore.sh                  #script to run in pod
    BR_JOB=cloud-pak-restore                  #Job name to be used
    BR_PVC=cloud-pak-restore-status           #PVC name to be used
fi

show_br_output() {
SLEEP_TIME=60
export temp_dir=$(mktemp -d)
while true; do
    # Check if Cloud Pak br job is active
    br_status=$(oc get job ${BR_JOB} -n cloud-pak-br -o jsonpath='{.status.active}' 2>/dev/null)
    if [ "${br_status}" == "1" ];then
        echo "Cloud Pak ${operation} job is ACTIVE"
    else
        echo "Cloud Pak ${operation} job is NOT ACTIVE"
    fi
    echo

    # Now retrieve logs if the br is still active
    br_status=$(oc get job ${BR_JOB} -n cloud-pak-br -o jsonpath='{.status.active}' 2>/dev/null)
    if [ "${br_status}" == "1" ];then
        BR_POD=$(oc get po -n cloud-pak-br --no-headers -l app=cloud-pak-br | head -1 | awk '{print $1}')
        oc logs ${BR_POD} --tail=100
    else
        break
    fi

    echo "${operation} is ACTIVE, Sleeping for ${SLEEP_TIME} seconds..."
    echo "-----------------------------------------------------------"
    sleep ${SLEEP_TIME}
done
}

# Check if the br job is still running, it must not exist
if [ "$(oc get job ${BR_JOB} -n cloud-pak-br -o jsonpath='{.status.active}' 2>/dev/null)" == "1" ];then
    echo "${operation} job is still present in the cloud-pak-br project. Will show progress instead of starting the ${operation}."
    show_br_output
    echo "success"
    exit 0
fi

# Just in case the job exists and it has completed or is in invalid state, delete it
oc delete job -n cloud-pak-br ${BR_JOB} 2>/dev/null

# Temporary: set storage class to use for the BR job
if oc get sc managed-nfs-storage > /dev/null 2>&1;then
    export BR_SC=managed-nfs-storage
elif oc get sc ocs-storagecluster-cephfs > /dev/null 2>&1;then
    export BR_SC=ocs-storagecluster-cephfs
elif oc get sc ibmc-file-gold-gid > /dev/null 2>&1;then
    export BR_SC=ibmc-file-gold-gid
else
    echo "No supported storage class found for the ${operation} job, exiting."
    exit 1
fi

# Create and populate the configmap with the configuration
echo "Setting the ${operation} configuration..."
oc delete cm -n cloud-pak-br cloud-pak-br-config --ignore-not-found
oc create cm -n cloud-pak-br cloud-pak-br-config 2>/dev/null
# Conditionally set the CP4D configuration
if [[ "${cpak}" == *"cp4d"* ]];then
    oc set data -n cloud-pak-br cm/cloud-pak-br-config --from-file=./cp4d-config.yaml
fi
# Conditionally set the CP4I configuration
if [[ "${cpak}" == *"cp4i"* ]];then
    oc set data -n cloud-pak-br cm/cloud-pak-br-config --from-file=./cp4i-config.yaml
fi

# Always set the global and OpenShift configuration
oc set data -n cloud-pak-br cm/cloud-pak-br-config --from-file=./openshift-config.yaml

# Conditionally set the backup configuration
if [[ "${operation}" == *"backup"* ]];then
    # Create PVC for br job
    echo "Creating the PVC if not already present..."
    oc process -f cpdbr-pvc.yaml -p BR_SC=${BR_SC} -p BR_JOB=${BR_JOB} | oc apply -f -
    # Start br job
    echo "Starting the ${operation} job..."
    oc process -f cpdbr-job.yaml -p BR_SCRIPT=${BR_SCRIPT} -p BR_JOB=${BR_JOB} -p CPD_INSTANCE=${CPD_INSTANCE} -p CPD_OPERATOR_BACKUP=${CPD_OPERATOR_BACKUP} -p CPD_INSTANCE_BACKUP=${CPD_INSTANCE_BACKUP} | oc apply -f -
fi
# Conditionally set the restore configuration
# if [[ "${operation}" == *"restore"* ]];then
#     # Start restore job
# fi

waittime=0
pod_status=""
echo "Waiting until Cloud Pak ${operation} pod has Init:0/1 status..."
while [ "$pod_status" != "Init:0/1" ] && [ $waittime -lt 300 ];do
        sleep 5
        pod_status=$(oc get po --no-headers -l app=cloud-pak-br | head -1 | awk '{print $3}')
        echo "Cloud Pak ${operation} status: $pod_status"
        waittime=$((waittime+5))
done

if [ $waittime -ge 300 ];then
    echo "Timeout while waiting for Cloud Pak ${operation} pod to start"
    exit 1
fi

BR_POD=$(oc get po -n cloud-pak-br --no-headers -l app=cloud-pak-br | head -1 | awk '{print $1}')

command_exit=1
waittime=0
echo "Waiting until the pod accepts commands..."
while [ "$command_exit" != "0" ] && [ $waittime -lt 300 ];do
        sleep 5
        oc rsh -c wait-config $BR_POD touch /tmp/command-accepted 2> /dev/null
        command_exit=$?
        waittime=$((waittime+5))
done

if [ $waittime -ge 300 ];then
    echo "Timeout while waiting for Cloud Pak ${operation} pod to accept commmands"
    exit 1
fi

#Copy br script
echo "Coping ${operation} script to ${operation} pod..."
chmod +x ${BR_SCRIPT}
oc cp ${BR_SCRIPT} ${BR_POD}:/Data/cpd-status/ -c wait-config

# Start the br
echo "Starting the ${operation}..."
oc rsh -c wait-config $BR_POD bash -c 'touch /tmp/cpd-config-ready; chmod 777 /tmp/cpd-config-ready'

# Wait a few seconds for the br container to start
sleep 5

# Show br status
show_br_output
echo "success"
exit 0
