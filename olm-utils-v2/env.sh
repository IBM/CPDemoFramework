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
fi


oc new-project cloud-pak-deployer
oc project cloud-pak-deployer
oc create serviceaccount cloud-pak-deployer-sa
oc adm policy add-scc-to-user privileged -z cloud-pak-deployer-sa
oc adm policy add-cluster-role-to-user cluster-admin -z cloud-pak-deployer-sa

oc apply -f deployer-job.yaml

waittime=0
while [ "$pod_schedule_status" != "True" ] && [ $waittime -lt 300 ];do
        sleep 5
        pod_schedule_status=$(oc get po --no-headers -l app=cloud-pak-deployer -o 'jsonpath={..status.conditions[?(@.type=="PodScheduled")].status}')
        echo "Cloud Pak Deployer scheduled: $pod_schedule_status"
        waittime=$((waittime+5))
done

CONFIG_DIR=./cpd-config && mkdir -p $CONFIG_DIR/config
cp cpd-config.yaml $CONFIG_DIR/config
STATUS_DIR=./cpd-status && mkdir -p $STATUS_DIR

DEPLOYER_POD=$(oc get po --no-headers -l app=cloud-pak-deployer | head -1 | awk '{print $1}')
oc cp -c wait-config $CONFIG_DIR $DEPLOYER_POD:/Data/cpd-config/

oc rsh -c wait-config $DEPLOYER_POD /cloud-pak-deployer/cp-deploy.sh vault set \
  -vs ibm_cp_entitlement_key -vsv "$ICR_KEY"

oc rsh -c wait-config $DEPLOYER_POD /cloud-pak-deployer/cp-deploy.sh vault set \
  -vs cpd-demo-oc-login -vsv "oc login --server=$SERVER --token=$API_TOKEN"

oc rsh -c wait-config $DEPLOYER_POD /cloud-pak-deployer/cp-deploy.sh vault list

# Start the deployer
echo "Starting the deployer"
oc rsh -c wait-config $DEPLOYER_POD bash -c 'touch /Data/cpd-config/config-ready; chmod 777 /Data/cpd-config/config-ready'

# Wait a few seconds for the deployer container to start
sleep 5

# Follow the logs
oc logs -f $DEPLOYER_POD