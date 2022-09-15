#!/bin/sh
echo "Deleting Deployer job..."
oc delete job -n cloud-pak-deployer cloud-pak-deployer