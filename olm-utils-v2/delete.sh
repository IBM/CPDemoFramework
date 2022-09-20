#!/bin/sh
echo "Deleting Deployer job..."
oc delete job -n cloud-pak-deployer cloud-pak-deployer
if [ "$(oc get job cloud-pak-deployer -n cloud-pak-deployer -o jsonpath='{.status.active}' 2>/dev/null)" != "1" ];then
    echo "success"
fi
