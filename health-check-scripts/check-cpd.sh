json=$1
 
readJsonConfig() {
        echo $json | jq -r $1
}

$(readJsonConfig ".oc_login")
CP4D_PROJECT=$(readJsonConfig ".cp4d_project_name")

oc get "project/cpd" > /dev/null 2>&1

if [ "$?" != "0" ]; then
    echo "CP4D installation not found"
    exit 0
fi

echo "CP4D is installed!"

#!/bin/bash
SCRIPT_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )

get_logtime() {
  echo $(date "+%Y-%m-%d %H:%M:%S")
}

log() {
  LOG_TIME=$(get_logtime)
  printf "[${LOG_TIME}] ${1}\n"
}

CP4D_PROJECT="cpd"

if [ -z "${CP4D_PROJECT}" ];then
    echo "Usage: $0 <cp4d-project>"
    exit 1
fi

temp_dir=$(mktemp -d)
log "Getting Custom Resources in OpenShift project ${CP4D_PROJECT}..."
oc get --no-headers -n $CP4D_PROJECT $(oc api-resources --namespaced=true --verbs=list -o name | grep ibm | awk '{printf "%s%s",sep,$0;sep=","}')  --ignore-not-found -o=custom-columns=KIND:.kind,NAME:.metadata.name --sort-by='kind' > ${temp_dir}/cp4d-resources.out
while read -r line;do
    read -r CR CR_NAME <<< "${line}"
    case $CR in
        Ibmcpd|CommonService|OperandRequest)
        ;;
        *)
        cr_status=$(oc get -n $CP4D_PROJECT $CR $CR_NAME -o jsonpath='{.status}' | jq -r '. | to_entries | map(select(.key | match("Status"))) | map(.value) | first')
        if [[ "${cr_status}" != "" ]] && [[ ${cr_status} != "null" ]];then
            echo "${CR} - ${CR_NAME} - ${cr_status}"
        fi
        ;;
    esac
done < ${temp_dir}/cp4d-resources.out

exit 0
