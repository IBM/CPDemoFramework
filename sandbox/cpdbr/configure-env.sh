#!/bin/sh

# Retrieve parameters
ICR=$1
SERVER=$2
API_TOKEN=$3
KUBEADMIN_USER=$4
KUBEADMIN_PASS=$5
S3_URL=$6
BUCKET=$7
REGION=$8
ACCESS_KEY=$9
ACCESS_ID=$10

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
echo "success"

# Store variables in shell script
echo "ICR=$ICR" >> .env
echo "S3_URL=$S3_URL" >> .env
echo "BUCKET=$BUCKET" >> .env
echo "REGION=$REGION" >> .env
echo "ACCESS_KEY=$ACCESS_KEY" >> .env
echo "ACCESS_ID=$ACCESS_ID" >> .env
echo "API_TOKEN=$API_TOKEN" >> .env
echo "KUBEADMIN_USER=$KUBEADMIN_USER" >> .env
echo "KUBEADMIN_PASS=$KUBEADMIN_PASS" >> .env
echo "SERVER=$SERVER" >> .env

echo "[default]" > credentials-velero.txt
echo "\naws_access_key_id=$ACCESS_ID" >> credentials-velero.txt
echo "aws_secret_access_key=$ACCESS_KEY" >> credentials-velero.txt
chmod +x .env

echo "##### Configuring the cluster #####"

# Get the updated config file from cloud-pak-br-config
oc extract -n cloud-pak-br  cm/cloud-pak-br-config --to=. --confirm 2>/dev/null
if [ $? != 0 ];then
    echo "cloud-pak-br-config does not exist! it will be created in the next step!."
else
    echo "cloud-pak-br-config already exists in the cluster! The script will make use of the same file!"
fi

echo "Creating oadp-operator namespace..."
oc create namespace oadp-operator
oc annotate namespace oadp-operator openshift.io/node-selector=""

# Check if (secret)credentials-velero already exists
# if it exists update the secret
oc get secret cloud-credentials -n oadp-operator
if [ $? != 0 ];then
    echo "Secret already exists, updating it"
    oc create secret generic cloud-credentials --namespace oadp-operator --from-file cloud=./credentials-velero.txt --dry-run=client -o yaml | oc apply -f -
else
    echo "Creating secret..."
    oc create secret generic cloud-credentials --namespace oadp-operator --from-file cloud=./credentials-velero.txt
fi

echo "Installing OADP Operator..."
oc apply -f oadp-operatorgroup.yaml
oc apply -f oadp-sub.yaml
sleep 30
echo "Creating DPA..."
oc project oadp-operator
oc process -f oadp-dpa.yaml -p BUCKET=${BUCKET} -p REGION=${REGION} -p S3_URL=${S3_URL} | oc apply -f -


echo "Setting up the backup execution pod..."
oc new-project cloud-pak-br 2> /dev/null
oc project cloud-pak-br 2>&1 > /dev/null
oc create serviceaccount cloud-pak-br-sa 2> /dev/null
oc adm policy add-scc-to-user privileged -z cloud-pak-br-sa
oc adm policy add-cluster-role-to-user cluster-admin -z cloud-pak-br-sa

# oc create cm -n cloud-pak-br cloud-pak-br-config 2>/dev/null


# pull secret
# oc get secret/pull-secret -n openshift-config --template='{{index .data ".dockerconfigjson" | base64decode}}' > source-secret.json
