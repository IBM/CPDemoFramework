#!/bin/bash

source ./env-vars.sh

source ./functions.sh

#cloud pak(s)
cpak=$1
CPAK_ADMIN_PASSWORD=$2
CPAK_ENV_NAME=$3

echo "CPAK_ADMIN_PASSWORD=$CPAK_ADMIN_PASSWORD" >> ./env-vars.sh
echo "CPAK_ENV_NAME=$CPAK_ENV_NAME" >> ./env-vars.sh

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
    # Check if Cloud Pak Deployer job is active
    deployer_status=$(oc get job cloud-pak-deployer -n cloud-pak-deployer -o jsonpath='{.status.active}' 2>/dev/null)
    if [ "${deployer_status}" == "1" ];then
        log "Cloud Pak Deployer job is ACTIVE"
    else
        log "Cloud Pak Deployer job is NOT ACTIVE"
    fi
    echo

    # Get current stage of the deployer
    current_stage=$(oc logs -n cloud-pak-deployer job/cloud-pak-deployer | grep -E 'PLAY \[' | tail -1)
    log "Current stage: ${current_stage}"
    echo
    # Get current task of the deployer
    current_task=$(oc logs -n cloud-pak-deployer job/cloud-pak-deployer | grep -E 'TASK \[' | tail -1)
    log "Current task: ${current_task}"
    echo
    # Get catalog sources
    log "Listing catalog sources"
    oc get catsrc -n openshift-marketplace --no-headers -o custom-columns=':.metadata.name'
    echo
    # Listing subscriptions
    log "Listing IBM subscriptions"
    oc get sub -n ibm-common-services --no-headers -o custom-columns=':.metadata.name'
    echo
    # Listing CSVs
    log "Listing CSVs"
    oc get csv -n ibm-common-services --no-headers -o custom-columns=':.metadata.name'
    echo

    # Now do Cloud Pak specific checks
    if [[ "${cpak}" == *"cp4d"* ]];then
        ./deploy-status-cp4d.sh
    fi
    if [[ "${cpak}" == *"cp4i"* ]];then
        ./deploy-status-cp4i.sh
    fi

    # Now retrieve logs if the deployer is still active
    deployer_status=$(oc get job cloud-pak-deployer -n cloud-pak-deployer -o jsonpath='{.status.active}' 2>/dev/null)
    if [ "${deployer_status}" == "1" ];then
        DEPLOYER_POD=$(oc get po -n cloud-pak-deployer --no-headers -l app=cloud-pak-deployer | head -1 | awk '{print $1}')
        log "Retrieving deployer logs into ./log"
        mkdir -p log
        oc cp -n cloud-pak-deployer -c cloud-pak-deployer \
            ${DEPLOYER_POD}:/Data/cpd-status/log ./log/ 2>/dev/null 1>&2
    else
        failed_status=$(oc get job -n cloud-pak-deployer cloud-pak-deployer -o jsonpath='{.status.failed}' 2>/dev/null)
        succeeded_status=$(oc get job -n cloud-pak-deployer cloud-pak-deployer -o jsonpath='{.status.succeeded}' 2>/dev/null)
        if [[ ${failed_status} == "1" ]];then
            log "Cloud Pak deployer FAILED, check the logs in the ${PWD}/log directory"
        elif [[ ${succeeded_status} == "1" ]];then
            log "Cloud Pak deployer completed SUCCESSFULLY"
        fi
        break
    fi

    log "Deployer is ACTIVE, Sleeping for ${SLEEP_TIME} seconds..."
    log "-----------------------------------------------------------"
    sleep ${SLEEP_TIME}
done
}

# Check if the deployer job is still running, it must not exist
if [ "$(oc get job cloud-pak-deployer -n cloud-pak-deployer -o jsonpath='{.status.active}' 2>/dev/null)" == "1" ];then
    echo "Deployer job is still present in the cloud-pak-deployer project. Will show progress instead of starting the deployer."
    show_deployer_output
    exit 0
fi

# Just in case the job exists and it has completed or is in invalid state, delete it
oc delete job -n cloud-pak-deployer cloud-pak-deployer 2>/dev/null

# Temporary: set storage class to use for the deployer job
if oc get sc managed-nfs-storage > /dev/null 2>&1;then
    export DEPLOYER_SC=managed-nfs-storage
elif oc get sc ocs-storagecluster-cephfs > /dev/null 2>&1;then
    export DEPLOYER_SC=ocs-storagecluster-cephfs
elif oc get sc ibmc-file-gold-gid > /dev/null 2>&1;then
    export DEPLOYER_SC=ibmc-file-gold-gid
else
    echo "No supported storage class found for the deployer job, exiting."
    exit 1
fi

# Create and populate the configmap with the configuration
echo "Setting the deployer configuration..."
oc delete cm -n cloud-pak-deployer cloud-pak-deployer-config --ignore-not-found
oc create cm -n cloud-pak-deployer cloud-pak-deployer-config 2>/dev/null
# Conditionally set the CP4D configuration
if [[ "${cpak}" == *"cp4d"* ]];then
    oc set data -n cloud-pak-deployer cm/cloud-pak-deployer-config --from-file=./cp4d-config.yaml
fi
# Conditionally set the CP4I configuration
if [[ "${cpak}" == *"cp4i"* ]];then
    oc set data -n cloud-pak-deployer cm/cloud-pak-deployer-config --from-file=./cp4i-config.yaml
fi

# Always set the global and OpenShift configuration
if [[ "${CPAK_ENV_NAME}" != "" ]];then
    sed -i "s/{{ env_id }}/${CPAK_ENV_NAME}/g" ./openshift-config.yaml
fi
oc set data -n cloud-pak-deployer cm/cloud-pak-deployer-config --from-file=./openshift-config.yaml

# Create PVC for deployer job
echo "Creating the PVC if not already present..."
oc process -f deployer-pvc.yaml -p DEPLOYER_SC=${DEPLOYER_SC} | oc apply -f -

# Start deployer job
echo "Starting the deployer job..."
if [[ "${CPAK_ADMIN_PASSWORD}" == "" ]];then
    oc process -f deployer-job.yaml \
        -p CP_ENTITLEMENT_KEY="$ICR_KEY" \
        -p OC_LOGIN_COMMAND="$OC_LOGIN_COMMAND" | oc apply -f -
else
    oc process -f deployer-job-with-admin.yaml \
        -p CP_ENTITLEMENT_KEY="$ICR_KEY" \
        -p OC_LOGIN_COMMAND="$OC_LOGIN_COMMAND" \
        -p CPAK_ADMIN_PASSWORD="${CPAK_ADMIN_PASSWORD}" | oc apply -f -
fi

# Start a debug job (sleep infinity) so that we can easily get access to the deployer logs
echo "Starting the deployer debug job..."
oc apply -f deployer-debug-job.yaml

# Wait a few seconds for the deployer container to start
sleep 5

# Show deployer status
show_deployer_output
echo "success"
echo "all done"
exit 0