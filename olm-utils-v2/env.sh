#!/bin/sh
SERVER=

# APITOKEN
API_TOKEN=

# OR

# Username and password
KUBEADMIN_USER=
KUBEADMIN_PASS=

# ICR KEY
# Please enter the ICR KEY if the server value is pointing to IBM cloud ROKS cluster.
ICR_KEY=

# SCRIPT
#Pod login and auto login to oc cluster from runutils
if  [ -n "$KUBEADMIN_USER" ] && [ -n "$KUBEADMIN_PASS" ]
    then
        alias oclogin_auto="run_utils login-to-ocp -u ${KUBEADMIN_USER} -p ${KUBEADMIN_PASS} --server=${SERVER}";
        alias pod_login="oc login -u ${KUBEADMIN_USER} -p ${KUBEADMIN_PASS} --server ${SERVER}";
    else
        if  [ -z "$API_TOKEN" ]
            then
                    echo "Invalid api token, please check env.sh file";
            else
                alias pod_login="oc login --token=${API_TOKEN} --server=${SERVER}";
                alias oclogin_auto="run_utils login-to-ocp --token=${API_TOKEN} --server=${SERVER}";
        fi
fi
# Pod login
pod_login

# Check if the last command executed properly
if [ $? -eq 0 ]; then
    echo "Logged in Successfully";
else
    echo "Login Failed";
    exit 1
fi

# Check if the deployer job is still running, it must not exist
if oc get job cloud-pak-deployer -n cloud-pak-deployer > /dev/null 2>&1;then
    echo "Deployer job is still present in the cloud-pak-deployer project. Will show progress instead of starting the deployer."
    sleep 1
    oc logs -f -n cloud-pak-deployer job/cloud-pak-deployer
    exit 0
fi

# Temporary: set storage class to use for the deployer job
if oc get sc managed-nfs-storage > /dev/null 2>&1;then
    export DEPLOYER_SC=managed-nfs-storage
elif oc get sc ocs-storagecluster-cephfs > /dev/null 2>&1;then
    export DEPLOYER_SC=ocs-storagecluster-cephfs
else
    echo "No supported storage class found for the deployer job, exiting."
    exit 1
fi

# Wait until the deployer image has been built
echo "Wait for image to be built and pushed to internal registry..."
waittime=0
while ! oc get istag -n cloud-pak-deployer cloud-pak-deployer:latest 2>/dev/null && [ $waittime -lt 300 ];do
    sleep 5
done
if [ $waittime -ge 300 ];then
    echo "Timeout while waiting for Cloud Pak Deployer image to be built"
    exit 1
fi

# Create and populate the configmap with the configuration
echo "Setting the deployer configuration..."
oc create cm -n cloud-pak-deployer cloud-pak-deployer-config 2>/dev/null
oc set data -n cloud-pak-deployer cm/cloud-pak-deployer-config --from-file=./cpd-config.yaml

# Create PVC for deployer job
echo "Creating the PVC if not already present..."
oc process -f deployer-pvc.yaml | oc apply -f -

# Start deployer job
echo "Starting the deployer job..."
oc apply -f deployer-job.yaml

waittime=0
pod_status=""
echo "Waiting until Cloud Pak Deployer pod has Init:0/1 status..."
while [ "$pod_status" != "Init:0/1" ] && [ $waittime -lt 300 ];do
        sleep 5
        pod_status=$(oc get po --no-headers -l app=cloud-pak-deployer | head -1 | awk '{print $3}')
        echo "Cloud Pak Deployer status: $pod_status"
        waittime=$((waittime+5))
done

if [ $waittime -ge 300 ];then
    echo "Timeout while waiting for Cloud Pak Deployer pod to start"
    exit 1
fi

DEPLOYER_POD=$(oc get po -n cloud-pak-deployer --no-headers -l app=cloud-pak-deployer | head -1 | awk '{print $1}')

command_exit=1
waittime=0
echo "Waiting until the pod accepts commands..."
while [ "$command_exit" != "0" ] && [ $waittime -lt 300 ];do
        sleep 5
        oc rsh -c wait-config $DEPLOYER_POD touch /tmp/command-accepted 2> /dev/null
        command_exit=$?
        waittime=$((waittime+5))
done

if [ $waittime -ge 300 ];then
    echo "Timeout while waiting for Cloud Pak Deployer pod to accept commmands"
    exit 1
fi

oc rsh -c wait-config $DEPLOYER_POD /cloud-pak-deployer/cp-deploy.sh vault set \
  -vs ibm_cp_entitlement_key -vsv "$ICR_KEY"

oc rsh -c wait-config $DEPLOYER_POD /cloud-pak-deployer/cp-deploy.sh vault set \
  -vs cpd-demo-oc-login -vsv "oc login --server=$SERVER --token=$API_TOKEN"

oc rsh -c wait-config $DEPLOYER_POD /cloud-pak-deployer/cp-deploy.sh vault list

# Start the deployer
echo "Starting the deployer..."
oc rsh -c wait-config $DEPLOYER_POD bash -c 'touch /Data/cpd-config/config-ready; chmod 777 /Data/cpd-config/config-ready'

# Wait a few seconds for the deployer container to start
sleep 5

# Follow the logs
oc logs -n cloud-pak-deployer -f $DEPLOYER_POD