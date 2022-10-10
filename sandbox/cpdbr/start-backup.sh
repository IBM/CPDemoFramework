#!/bin/bash

source .env

# # source ./functions.sh

#cloud pak(s)
cpak=$1

# Check if we can access the cluster
oc cluster-info
# Check if the last command executed properly
if [ $? -ne 0 ]; then
    echo "OpenShift cluster is not accessible, make sure you run the configuration steps";
    exit 1
fi

show_deployer_output() {
SLEEP_TIME=300
export temp_dir=$(mktemp -d)
while true; do
    # Check if Cloud Pak backup job is active
    backup_status=$(oc get job cloud-pak-br -n cloud-pak-br -o jsonpath='{.status.active}' 2>/dev/null)
    if [ "${backup_status}" == "1" ];then
        log "Cloud Pak Backup job is ACTIVE"
    else
        log "Cloud Pak Backup job is NOT ACTIVE"
    fi
    echo

    # Get current stage of the backup
    current_stage=$(oc logs -n cloud-pak-br job/cloud-pak-br | grep -E 'PLAY \[' | tail -1)
    log "Current stage: ${current_stage}"
    echo
    # Get current task of the backup
    current_task=$(oc logs -n cloud-pak-br job/cloud-pak-br | grep -E 'TASK \[' | tail -1)
    log "Current task: ${current_task}"
    echo
    # # Get catalog sources
    # log "Listing catalog sources"
    # oc get catsrc -n openshift-marketplace --no-headers -o custom-columns=':.metadata.name'
    # echo
    # # Listing subscriptions
    # log "Listing IBM subscriptions"
    # oc get sub -n ibm-common-services --no-headers -o custom-columns=':.metadata.name'
    # echo
    # # Listing CSVs
    # log "Listing CSVs"
    # oc get csv -n ibm-common-services --no-headers -o custom-columns=':.metadata.name'
    # echo

    # Now do Cloud Pak specific checks
    # if [[ "${cpak}" == *"cp4d"* ]];then
    #     ./deploy-status-cp4d.sh
    # fi
    # if [[ "${cpak}" == *"cp4i"* ]];then
    #     ./deploy-status-cp4i.sh
    # fi

    # Now retrieve logs if the backup is still active
    backup_status=$(oc get job cloud-pak-br -n cloud-pak-br -o jsonpath='{.status.active}' 2>/dev/null)
    if [ "${backup_status}" == "1" ];then
        BACKUP_POD=$(oc get po -n cloud-pak-br --no-headers -l app=cloud-pak-br | head -1 | awk '{print $1}')
        log "Retrieving Backup logs into ./log"
        mkdir -p log
        oc cp -n cloud-pak-br -c cloud-pak-br \
            ${BACKUP_POD}:/Data/cpd-status/log ./log/
    else
        break
    fi

    log "Deployer is ACTIVE, Sleeping for ${SLEEP_TIME} seconds..."
    log "-----------------------------------------------------------"
    sleep ${SLEEP_TIME}
done
}

# Check if the backup job is still running, it must not exist
if [ "$(oc get job cloud-pak-br -n cloud-pak-br -o jsonpath='{.status.active}' 2>/dev/null)" == "1" ];then
    echo "Backup job is still present in the cloud-pak-br project. Will show progress instead of starting the backup."
    show_deployer_output
    exit 0
fi

# Just in case the job exists and it has completed or is in invalid state, delete it
oc delete job -n cloud-pak-br cloud-pak-br 2>/dev/null

# Temporary: set storage class to use for the backup job
if oc get sc managed-nfs-storage > /dev/null 2>&1;then
    export BACKUP_SC=managed-nfs-storage
elif oc get sc ocs-storagecluster-cephfs > /dev/null 2>&1;then
    export BACKUP_SC=ocs-storagecluster-cephfs
elif oc get sc ibmc-file-gold-gid > /dev/null 2>&1;then
    export BACKUP_SC=ibmc-file-gold-gid
else
    echo "No supported storage class found for the deployer job, exiting."
    exit 1
fi

# Create and populate the configmap with the configuration
echo "Setting the backup configuration..."
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

# Create PVC for backup job
echo "Creating the PVC if not already present..."
oc process -f br-pvc.yaml -p BACKUP_SC=${BACKUP_SC} | oc apply -f -

# Start deployer job
echo "Starting the deployer job..."
oc apply -f br-job.yaml

waittime=0
pod_status=""
echo "Waiting until Cloud Pak Backup pod has Init:0/1 status..."
while [ "$pod_status" != "Init:0/1" ] && [ $waittime -lt 300 ];do
        sleep 5
        pod_status=$(oc get po --no-headers -l app=cloud-pak-br | head -1 | awk '{print $3}')
        echo "Cloud Pak Backup status: $pod_status"
        waittime=$((waittime+5))
done

if [ $waittime -ge 300 ];then
    echo "Timeout while waiting for Cloud Pak Backup pod to start"
    exit 1
fi

BACKUP_POD=$(oc get po -n cloud-pak-br --no-headers -l app=cloud-pak-br | head -1 | awk '{print $1}')

command_exit=1
waittime=0
echo "Waiting until the pod accepts commands..."
while [ "$command_exit" != "0" ] && [ $waittime -lt 300 ];do
        sleep 5
        oc rsh -c wait-config $BACKUP_POD touch /tmp/command-accepted 2> /dev/null
        command_exit=$?
        waittime=$((waittime+5))
done

if [ $waittime -ge 300 ];then
    echo "Timeout while waiting for Cloud Pak Backup pod to accept commmands"
    exit 1
fi


# not running cp-deploy.sh in the backup pod
# oc rsh -c wait-config $BACKUP_POD /cloud-pak-deployer/cp-deploy.sh vault set \
#   -vs ibm_cp_entitlement_key -vsv "$ICR_KEY"

# oc rsh -c wait-config $BACKUP_POD /cloud-pak-deployer/cp-deploy.sh vault set \
#   -vs cpd-demo-oc-login -vsv "oc login --server=$SERVER --token=$API_TOKEN"

# oc rsh -c wait-config $BACKUP_POD /cloud-pak-deployer/cp-deploy.sh vault list

# Start the deployer
echo "Starting the backup..."
oc rsh -c wait-config $BACKUP_POD bash -c 'touch /tmp/cpd-config-ready; chmod 777 /tmp/cpd-config-ready'

# # Wait a few seconds for the deployer container to start
# sleep 5

# Show deployer status
show_deployer_output
echo "success"
echo "all done"
exit 0