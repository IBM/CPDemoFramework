#!/bin/bash

source ./.env
source ../../olm-utils-v2/functions.sh

#cloud pak(s)
cpak=$1
#backup or restore operation
operation=$2

backupName=$3

# Check if we can access the cluster
oc cluster-info
# Check if the last command executed properly
if [ $? -ne 0 ]; then
    echo "OpenShift cluster is not accessible, make sure you run the configuration steps";
    exit 1
fi

# Check which project is used for CP4D (it used to be cpd-instance, changing to cpd)
# Namespace where cpd is installed
if oc get project cpd >/dev/null 2>&1;then 
    CPD_INSTANCE=cpd
else
    CPD_INSTANCE=cpd-instance
fi

# Conditionally set the backup configuration
if [[ "${operation}" == *"backup"* ]];then
    BR_SCRIPT=pod-backup.sh                     #script to run in pod
    BR_JOB=cloud-pak-backup                     #Job name to be used
    CPD_INSTANCE_BACKUP=${backupName}-instance  #cpd instance backup will be saved with this name
    CPD_OPERATOR_BACKUP=${backupName}-operator  #cpd operator backup will be saved with this name
fi
# Conditionally set the restore configuration
if [[ "${operation}" == *"restore"* ]];then
    BR_SCRIPT=pod-restore.sh                  #script to run in pod
    BR_JOB=cloud-pak-restore                  #Job name to be used
    CPD_INSTANCE_BACKUP=${backupName}-instance  #cpd instance backup will be saved with this name
    CPD_OPERATOR_BACKUP=${backupName}-operator  #cpd operator backup will be saved with this name
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
if [[ "${operation}" == *"restore"* ]];then
    # Create PVC for br job
    echo "Creating the PVC if not already present..."
    oc process -f cpdbr-pvc.yaml -p BR_SC=${BR_SC} -p BR_JOB=${BR_JOB} | oc apply -f -
    # Start br job
    echo "Starting the ${operation} job..."
    oc process -f cpdbr-job.yaml -p BR_SCRIPT=${BR_SCRIPT} -p BR_JOB=${BR_JOB} -p CPD_INSTANCE=${CPD_INSTANCE} -p CPD_OPERATOR_BACKUP=${CPD_OPERATOR_BACKUP} -p CPD_INSTANCE_BACKUP=${CPD_INSTANCE_BACKUP} | oc apply -f -

fi

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

oc rsh -c wait-config $BR_POD /cloud-pak-deployer/cp-deploy.sh vault set \
 -vs ibm_cp_entitlement_key -vsv "$ICR"
oc rsh -c wait-config $BR_POD /cloud-pak-deployer/cp-deploy.sh vault set \
 -vs cpd-demo-oc-login -vsv "oc login --server=$SERVER --token=$API_TOKEN"
oc rsh -c wait-config $BR_POD /cloud-pak-deployer/cp-deploy.sh vault list


# Start a debug job (sleep infinity) so that we can easily get access to the br logs
echo "Starting the cpdbr debug job..."
oc apply -f cpdbr-debug-job.yaml

#Copy br script
echo "Copying ${operation} script and configuration yamls to ${operation} pod..."
chmod +x ${BR_SCRIPT}
oc cp ${BR_SCRIPT} ${BR_POD}:/Data/cpd-status/ -c wait-config
oc cp cp4d-config.yaml ${BR_POD}:/Data/cpd-config/ -c wait-config
oc cp openshift-config.yaml ${BR_POD}:/Data/cpd-config/ -c wait-config

# Start the br
echo "Starting the ${operation}..."
oc rsh -c wait-config $BR_POD bash -c 'touch /tmp/cpd-config-ready; chmod 777 /tmp/cpd-config-ready'

# Wait a few seconds for the br container to start
sleep 5

# Show br status
show_br_output
# Condition to display deployment credentials incase of restore 
if [[ "${operation}" == *"restore"* ]];then
    deployment_host=$(oc get route -n ${CPD_INSTANCE} cpd -o jsonpath='{.spec.host}' 2> /dev/null)
    deployment_admin_password=$(oc extract -n ${CPD_INSTANCE} secret/admin-user-details --to=- 2>/dev/null)
    if [ "${deployment_host}" != "" ];then
        log "Cloud Pak URL: https://${deployment_host}"
        log "Cloud Pak admin password: ${deployment_admin_password}"
    fi
fi
echo "success"
exit 0
