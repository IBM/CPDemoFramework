#!/usr/bin/env python
import sys
import os
import yaml
from yaml.loader import SafeLoader

component=sys.argv[1]
component_list = component.split(',')

storage_vendor=sys.argv[2]

cp4d_version=sys.argv[3]

# Open the file and load the file
with open('cpd-config.yaml') as f:
    list_doc = yaml.safe_load(f)

list_doc["cp4d"][0]["cp4d_version"] = cp4d_version
if storage_vendor.lower()=='nfs':
    list_doc["openshift"][0]["openshift_storage"][0]["storage_name"]= "nfs-storage"
    list_doc["openshift"][0]["openshift_storage"][0]["storage_type"]= "nfs"

elif storage_vendor.lower()=='ocs':
    list_doc["openshift"][0]["openshift_storage"][0]["storage_name"]= "ocs-storage"
    list_doc["openshift"][0]["openshift_storage"][0]["storage_type"]= "ocs"

elif storage_vendor.lower()=='portworx':
    list_doc["openshift"][0]["openshift_storage"][0]["storage_name"]= "portworx-storage"
    list_doc["openshift"][0]["openshift_storage"][0]["storage_type"]= "portworx"

elif storage_vendor.lower()=='managed-nfs-storage':
    list_doc["openshift"][0]["openshift_storage"][0]["storage_name"]= "nfs-storage"
    list_doc["openshift"][0]["openshift_storage"][0]["storage_type"]= "nfs"

elif storage_vendor.lower()=='roks-classic':
    list_doc["openshift"][0]["openshift_storage"][0]["storage_name"] = "nfs-storage"
    list_doc["openshift"][0]["openshift_storage"][0]["storage_type"] = "nfs"

    list_doc["openshift"][0]["openshift_storage"][0]["ocp_storage_class_block"]= "ibmc-block-gold"
    list_doc["openshift"][0]["openshift_storage"][0]["ocp_storage_class_file"] = "ibmc-file-gold-gid"

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
