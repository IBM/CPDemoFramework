#!/bin/sh

# Retrieve parameters
SRC_SERVER=$1
SRC_API_TOKEN=$2
SRC_KUBEADMIN_USER=$3
SRC_KUBEADMIN_PASS=$4
ICR_KEY=$5
S3_URL=$6
BUCKET=$7
ACCESS_KEY=$8
ACCESS_ID=$9

# SCRIPT
#Pod login and auto login to oc cluster from runutils
if  [ -n "$SRC_KUBEADMIN_USER" ] && [ -n "$SRC_KUBEADMIN_PASS" ]
    then
        alias oclogin_auto="run_utils login-to-ocp -u ${SRC_KUBEADMIN_USER} -p ${SRC_KUBEADMIN_PASS} --server=${SRC_SERVER}";
        alias pod_login="oc login -u ${SRC_KUBEADMIN_USER} -p ${SRC_KUBEADMIN_PASS} --server ${SRC_SERVER}";
    else
        if  [ -z "$SRC_API_TOKEN" ]
            then
                    echo "Invalid api token, please check env.sh file";
            else
                alias pod_login="oc login --token=${SRC_API_TOKEN} --server=${SRC_SERVER}";
                alias oclogin_auto="run_utils login-to-ocp --token=${SRC_API_TOKEN} --server=${SRC_SERVER}";
        fi
fi

# Pod login
pod_login
if [ $? != 0 ];then
    echo "Error logging in to OpenShift, please check your credentials"
    exit 1
fi
echo "success"

# Store variables in shell script
echo "ICR_KEY=$ICR_KEY" > ./env-vars.sh
echo "S3_URL=$S3_URL" >> ./env-vars.sh
echo "BUCKET=$BUCKET" >> ./env-vars.sh
echo "ACCESS_KEY=$ACCESS_KEY" >> ./env-vars.sh
echo "ACCESS_ID=$ACCESS_ID" >> ./env-vars.sh
echo "SRC_API_TOKEN=$SRC_API_TOKEN" >> ./env-vars.sh
echo "SRC_KUBEADMIN_USER=$SRC_KUBEADMIN_USER" >> ./env-vars.sh
echo "SRC_KUBEADMIN_PASS=$SRC_KUBEADMIN_PASS" >> ./env-vars.sh
echo "SRC_SERVER=$SRC_SERVER" >> ./env-vars.sh
chmod +x ./env-vars.sh
