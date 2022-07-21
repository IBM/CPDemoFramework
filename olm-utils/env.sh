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


# Deploy olm_utils to cluster
export PROJECT_NAME='olm-utils'
oc create namespace ${PROJECT_NAME}
oc project ${PROJECT_NAME}
oc create serviceaccount olm-utils-sa
oc adm policy add-cluster-role-to-user cluster-admin system:serviceaccount:olm-utils:olm-utils-sa
oc apply -f deployment.yaml

# # Setting the aliases
alias run_utils="kubectl exec ${PROJECT_NAME} --";
alias oclogin="run_utils login-to-ocp";
alias get_pods="kubectl get pods -n $PROJECT_NAME";
# alias oclogin_auto="run_utils login-to-ocp --token=${API_TOKEN} --server=${SERVER}"
alias get_preview="kubectl cp $PROJECT_NAME/$PROJECT_NAME:/tmp/work/preview.sh ${CHE_PROJECTS_ROOT}/techzone/olm-utils/preview.sh"

if  [ -n "$ICR_KEY" ]
then
    run_utils add_icr_cred_to_global_pull_secret.sh $ICR_KEY
fi

