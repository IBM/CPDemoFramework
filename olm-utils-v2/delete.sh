#!/bin/sh
SCRIPT_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )

echo "Deleting Deployer job..."
oc delete job -n cloud-pak-deployer cloud-pak-deployer