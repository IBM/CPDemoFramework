#!/usr/bin/env python
import sys
import os
import yaml
from yaml.loader import SafeLoader
import json

path = sys.argv[1]
cpak = sys.argv[2]
# Dict of list of services already installed
serviceInstalled = {
    "parentId" : "service-list",
    "parentTagName": "ul",
    "elementToRender" : "li",
    "data" : []
}

#####################For cp4d get the installed services#####################
# Open & load the config file into a list
if cpak == "cp4d":
    with open('cpd-config.yaml') as f:
        list_doc = yaml.safe_load(f)
    #iterate the state of each instance in the config yaml to get installed services
    for x in range(0,len(list_doc["cp4d"][0]["cartridges"])):
        if "state" in list_doc["cp4d"][0]["cartridges"][x] and list_doc["cp4d"][0]["cartridges"][x]["state"]=="installed":
            serviceInstalled["data"].append(list_doc["cp4d"][0]["cartridges"][x]["name"])
#########################################################################

#####################For cp4i get installed services#####################
# Open & load the config file into a list
elif cpak == "cp4i":
    with open('cpi-config.yaml') as f:
        list_doc = yaml.safe_load(f)
    #iterate the state of each instance in the config yaml to get installed services
    for x in range(0,len(list_doc["cp4i"][0]["instances"])):
        if "state" in list_doc["cp4d"][0]["instances"][x] and list_doc["cp4i"][0]["instances"][x]["state"] == "installed":
            serviceInstalled["service"].append(list_doc["cp4i"][0]["instances"][x]["type"])
#########################################################################

# Serializing json
json_object = json.dumps(serviceInstalled, indent=4)
 
# Writing to the json
with open(path, "w") as outfile:
    outfile.write(json_object)
