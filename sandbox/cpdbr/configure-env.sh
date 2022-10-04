#!/bin/sh

# Retrieve parameters
SRC_SERVER=$1
SRC_API_TOKEN=$2
SRC_KUBEADMIN_USER=$3
SRC_KUBEADMIN_PASS=$4
ICR_KEY=$5
S3_URL=$6
BUCKET=$7
REGION=$8
ACCESS_KEY=$9
ACCESS_ID=$10

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
echo "ICR_KEY=$ICR_KEY" > .env
echo "S3_URL=$S3_URL" >> .env
echo "BUCKET=$BUCKET" >> .env
echo "REGION=$REGION" >> .env
echo "ACCESS_KEY=$ACCESS_KEY" >> .env
echo "ACCESS_ID=$ACCESS_ID" >> .env
echo "SRC_API_TOKEN=$SRC_API_TOKEN" >> .env
echo "SRC_KUBEADMIN_USER=$SRC_KUBEADMIN_USER" >> .env
echo "SRC_KUBEADMIN_PASS=$SRC_KUBEADMIN_PASS" >> .env
echo "SRC_SERVER=$SRC_SERVER" >> .env
echo "\naws_access_key_id=$ACCESS_ID" >> credentials-velero.txt
echo "aws_secret_access_key=$ACCESS_KEY" >> credentials-velero.txt
chmod +x .env
