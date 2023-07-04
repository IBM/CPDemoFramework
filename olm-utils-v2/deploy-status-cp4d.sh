#!/bin/bash

source ./functions.sh

# Check which project is used for CP4D (it used to be cpd-instance, changing to cpd)
if oc get project cpd >/dev/null 2>&1;then 
    CP4D_PROJECT=cpd
else
    CP4D_PROJECT=cpd-instance
fi

# Listing custom resources for Cloud Pak for Data
API_RESOURCES=$(oc api-resources --namespaced=true --verbs=list -o name | grep ibm | awk '{printf "%s%s",sep,$0;sep=","}')
if [ ! -z ${API_RESOURCES} ];then
    log "Getting Custom Resources in OpenShift project ${CP4D_PROJECT}..."
    oc get --no-headers -n $CP4D_PROJECT ${API_RESOURCES}  --ignore-not-found -o=custom-columns=KIND:.kind,NAME:.metadata.name --sort-by='kind' > ${temp_dir}/cp4d-resources.out
    while read -r line;do
        read -r CR CR_NAME <<< "${line}"
        case $CR in
            Ibmcpd|CommonService|OperandConfig|OperandRequest|OperandRegistry|OperandBindInfo|ResourcePlan|ZenExtension|IBMLicensingMetadata)
            ;;
            *)
            cr_status=$(oc get -n $CP4D_PROJECT $CR $CR_NAME -o jsonpath='{.status}' 2>/dev/null | jq -r '. | to_entries | map(select(.key | match("Status"))) | map(.value) | first')
            if [[ "${cr_status}" != "" ]] && [[ ${cr_status} != "null" ]];then
                echo "${CR} - ${CR_NAME} - ${cr_status}"
            fi
            ;;
        esac
    done < ${temp_dir}/cp4d-resources.out
    echo
fi
cp4d_host=$(oc get route -n ${CP4D_PROJECT} cpd -o jsonpath='{.spec.host}' 2> /dev/null)
cp4d_admin_password=$(oc extract -n ${CP4D_PROJECT} secret/admin-user-details --to=- 2>/dev/null)
if [ "${cp4d_host}" != "" ];then
    log "Cloud Pak for Data URL: https://${cp4d_host}"
    log "Cloud Pak for Data admin password: ${cp4d_admin_password}"
fi
