#!/bin/sh

source ./functions.sh

CP4I_PROJECT=cp4i

# Listing custom resources for Cloud Pak for Integration
API_RESOURCES=$(oc api-resources --namespaced=true --verbs=list -o name | grep ibm | awk '{printf "%s%s",sep,$0;sep=","}')
if [ ! -z ${API_RESOURCES} ];then
    log "Getting Custom Resources in OpenShift project ${CP4I_PROJECT}..."
    oc get --no-headers -n $CP4I_PROJECT ${API_RESOURCES}  --ignore-not-found -o=custom-columns=KIND:.kind,NAME:.metadata.name --sort-by='kind' > ${temp_dir}/cp4d-resources.out
    while read -r line;do
        read -r CR CR_NAME <<< "${line}"
        case $CR in
            CommonService|OperandRequest)
            ;;
            *)
            cr_status=$(oc get -n $CP4D_PROJECT $CR $CR_NAME -o jsonpath='{.status}' | jq -r '. | to_entries | map(select(.key | match("Status"))) | map(.value) | first')
            if [[ "${cr_status}" != "" ]] && [[ ${cr_status} != "null" ]];then
                echo "${CR} - ${CR_NAME} - ${cr_status}"
            fi
            ;;
        esac
    done < ${temp_dir}/cp4d-resources.out
    echo
fi

# Show host of CP4I navigator if it exists
cp4i_host=$(oc get route -n ${CP4I_PROJECT} cpd -o jsonpath='{.spec.host}' 2> /dev/null)
# Show password of CP4I navigator
cp4i_admin_password=$(oc extract -n ${CP4I_PROJECT} secret/admin-user-details --to=- 2>/dev/null)
if [ "${cp4i_host}" != "" ];then
    log "Cloud Pak for Integration URL: https://${cp4i_host}"
    log "Cloud Pak for Integration admin password: ${cp4i_admin_password}"
fi