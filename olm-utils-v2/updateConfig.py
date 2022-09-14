#!/usr/bin/env python
import sys
import yaml
from yaml.loader import SafeLoader

component=sys.argv[1]
component_list = component.split(',')
storage_vendor=sys.argv[2]
version=sys.argv[3]
cpak=sys.argv[4]

#update openshift configuration yaml
with open('openshift-config.yaml') as f:
    list_os = yaml.safe_load(f)

if storage_vendor.lower()=='nfs':
    list_os["openshift"][0]["openshift_storage"][0]["storage_name"]= "nfs-storage"
    list_os["openshift"][0]["openshift_storage"][0]["storage_type"]= "nfs"

elif storage_vendor.lower()=='ocs':
    list_os["openshift"][0]["openshift_storage"][0]["storage_name"]= "ocs-storage"
    list_os["openshift"][0]["openshift_storage"][0]["storage_type"]= "ocs"

elif storage_vendor.lower()=='portworx':
    list_os["openshift"][0]["openshift_storage"][0]["storage_name"]= "portworx-storage"
    list_os["openshift"][0]["openshift_storage"][0]["storage_type"]= "portworx"

elif storage_vendor.lower()=='managed-nfs-storage':
    list_os["openshift"][0]["openshift_storage"][0]["storage_name"]= "nfs-storage"
    list_os["openshift"][0]["openshift_storage"][0]["storage_type"]= "nfs"

elif storage_vendor.lower()=='roks-classic':
    list_os["openshift"][0]["openshift_storage"][0]["storage_name"] = "nfs-storage"
    list_os["openshift"][0]["openshift_storage"][0]["storage_type"] = "nfs"

    list_os["openshift"][0]["openshift_storage"][0]["ocp_storage_class_block"]= "ibmc-block-gold"
    list_os["openshift"][0]["openshift_storage"][0]["ocp_storage_class_file"] = "ibmc-file-gold-gid"

    with open("openshift-config.yaml", "w") as f:
        yaml.dump(list_os, f, sort_keys=False)

#update cp4i congifuration yaml
if(cpak.lower()=='cp4i'):
    with open('cp4i-config.yaml') as f:
        list_cp4i = yaml.safe_load(f)
    list_cp4i["cp4i"][0]["cp4i_version"] = version
    for x in range(0,len(list_cp4i["cp4i"][0]["instances"])):
        for y in range(0,len(component_list)):
            if list_cp4i["cp4i"][0]["instances"][x]["type"] == component_list[y]:
                list_cp4i["cp4i"][0]["instances"][x]["state"] = "installed"
                print(list_cp4i["cp4i"][0]["instances"][x])
                if(y<len(component_list)):
                    x=0
    with open("cp4i-config.yaml", "w") as f:
        yaml.dump(list_cp4i, f, sort_keys=False)

#update cp4d configuration yaml
if(cpak.lower()=='cp4d'):
    list_cp4d["cp4d"][0]["cp4d_version"] = version
    with open('cp4d-config.yaml') as f:
        list_cp4d = yaml.safe_load(f)
    for x in range(0,len(list_cp4d["cp4d"][0]["cartridges"])):
        for y in range(0,len(component_list)):
            if list_cp4d["cp4d"][0]["cartridges"][x]["name"] == component_list[y]:
                list_cp4d["cp4d"][0]["cartridges"][x]["state"] = "installed"
                print(list_cp4d["cp4d"][0]["cartridges"][x])
                if(y<len(component_list)):
                    x=0
    with open("cp4d-config.yaml", "w") as f:
        yaml.dump(list_cp4d, f, sort_keys=False)
