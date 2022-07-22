#!/usr/bin/env python
import sys
import os
import yaml
from yaml.loader import SafeLoader

component=sys.argv[1]
component_list = component.split(',')

storage_vendor=sys.argv[4]

# Open the file and load the file
with open('cpd-config.yaml') as f:
    list_doc = yaml.safe_load(f)

if storage_vendor=="NFS" or "nfs":
    list_doc["openshift"][0]["openshift_storage"][0]["storage_name"]="nfs-storage"
    list_doc["openshift"][0]["openshift_storage"][0]["storage_type"]= "nfs"

elif storage_vendor=="OCS" or "ocs":
    list_doc["openshift"][0]["openshift_storage"][0]["storage_name"]="ocs-storage"
    list_doc["openshift"][0]["openshift_storage"][0]["storage_type"]= "ocs"

elif storage_vendor=="portworx":
    list_doc["openshift"][0]["openshift_storage"][0]["storage_name"]="portworx-storage"
    list_doc["openshift"][0]["openshift_storage"][0]["storage_type"]= "portworx"

elif storage_vendor=="managed-nfs-storage":
    list_doc["openshift"][0]["openshift_storage"][0]["storage_name"]="nfs-storage"
    list_doc["openshift"][0]["openshift_storage"][0]["storage_type"]= "nfs"

i=0
for x in range(0,len(list_doc["cp4d"][0]["cartridges"])):
    for y in range(0,len(component_list)):
        if list_doc["cp4d"][0]["cartridges"][x]["name"] == component_list[y]:
            list_doc["cp4d"][0]["cartridges"][x]["state"] = "installed"
            print(list_doc["cp4d"][0]["cartridges"][x])
            if(y<len(component_list)):
                x=0

with open("cpd-config.yaml", "w") as f:
    yaml.dump(list_doc, f, sort_keys=False)
