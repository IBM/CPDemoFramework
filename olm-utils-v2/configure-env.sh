#!/bin/sh

# Retrieve parameters
SERVER=$1
API_TOKEN=$2
KUBEADMIN_USER=$3
KUBEADMIN_PASS=$4
ICR_KEY=$5

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
if [ $? != 0 ];then
    echo "Error logging in to OpenShift, please check your credentials"
    exit 1
fi

# Prepare cloud-pak-deployer project and start building the image
echo "Preparing cloud-pak-deployer project on the OpenShift cluster..."
oc new-project cloud-pak-deployer 2> /dev/null
oc project cloud-pak-deployer 2>&1 > /dev/null
oc create serviceaccount cloud-pak-deployer-sa 2> /dev/null
oc adm policy add-scc-to-user privileged -z cloud-pak-deployer-sa
oc adm policy add-cluster-role-to-user cluster-admin -z cloud-pak-deployer-sa