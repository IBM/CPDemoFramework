#!/bin/sh
SCRIPT_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )

server = sys.argv[1]
api_token = sys.argv[2]
kubeadmin_user = sys.argv[3]
kubeadmin_password = sys.argv[4]
icr_key = sys.argv[5]

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

# Check if Cloud Pak Deployer image must be built
if ! oc get istag -n cloud-pak-deployer cloud-pak-deployer:latest --no-headers 2> /dev/null;then 
    echo "Building Cloud Pak Deployer image on the cluster. You can already start the configuration..."

cat << EOF | oc apply -f -
apiVersion: image.openshift.io/v1
kind: ImageStream
metadata:
  name: cloud-pak-deployer
spec:
  lookupPolicy:
    local: true
EOF

cat << EOF | oc apply -f -
apiVersion: build.openshift.io/v1
kind: BuildConfig
metadata:
  name: cloud-pak-deployer-bc
  namespace: cloud-pak-deployer
spec:
  source:
    type: Git
    git:
      uri: https://github.com/IBM/cloud-pak-deployer
      ref: deployer-logs
  strategy:
    type: Docker                      
  output:
    to:
      kind: ImageStreamTag
      name: cloud-pak-deployer:latest
EOF

  oc delete build -n cloud-pak-deployer -l buildconfig=cloud-pak-deployer-bc
  oc start-build -n cloud-pak-deployer bc/cloud-pak-deployer-bc

  echo "Wait for image to be built and pushed to internal registry..."
  while ! oc get istag -n cloud-pak-deployer cloud-pak-deployer:latest 2>/dev/null;do
    sleep 1
  done
fi

# Update environment variables in env.sh scripot
python3.8 update-env-vars.py $SERVER $API_TOKEN $KUBEADMIN_USER $KUBEADMIN_PASS $ICR_KEY