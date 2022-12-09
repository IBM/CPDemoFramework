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

# Let the deployer find out the correct storage type
list_os["openshift"][0]["openshift_storage"][0]["storage_name"]= "auto-storage"
list_os["openshift"][0]["openshift_storage"][0]["storage_type"]= "auto"

with open("openshift-config.yaml", "w") as f:
    yaml.dump(list_os, f, sort_keys=False)

#update cp4i congifuration yaml
if cpak.lower()=='cp4i':
    with open('cp4i-config.yaml') as f:
        list_cp4i = yaml.safe_load(f)
    list_cp4i["cp4i"][0]["cp4i_version"] = version
    for x in range(0,len(list_cp4i["cp4i"][0]["instances"])):

        if "state" in list_cp4i["cp4i"][0]["instances"][x]:
            list_cp4i["cp4i"][0]["instances"][x]["state"] = "removed"
        # print(list_cp4i["cp4i"][0]["instances"][x])
        for y in range(0,len(component_list)):
            if list_cp4i["cp4i"][0]["instances"][x]["type"] == component_list[y]:
                list_cp4i["cp4i"][0]["instances"][x]["state"] = "installed"
                print(list_cp4i["cp4i"][0]["instances"][x])
                if(y<len(component_list)):
                    x=0
    with open("cp4i-config.yaml", "w") as f:
        yaml.dump(list_cp4i, f, sort_keys=False)

#update cp4d configuration yaml
elif cpak.lower()=='cp4d':
    with open('cp4d-config.yaml') as f:
        list_cp4d = yaml.safe_load(f)
    list_cp4d["cp4d"][0]["cp4d_version"] = version
    for x in range(0,len(list_cp4d["cp4d"][0]["cartridges"])):
        if "state" in list_cp4d["cp4d"][0]["cartridges"][x]:
            list_cp4d["cp4d"][0]["cartridges"][x]["state"] = "removed"
        for y in range(0,len(component_list)):
            if list_cp4d["cp4d"][0]["cartridges"][x]["name"] == component_list[y]:
                list_cp4d["cp4d"][0]["cartridges"][x]["state"] = "installed"
                print(list_cp4d["cp4d"][0]["cartridges"][x])
                if(y<len(component_list)):
                    x=0
    with open("cp4d-config.yaml", "w") as f:
        yaml.dump(list_cp4d, f, sort_keys=False)
print("success")