#!/usr/bin/env python
import sys
import os
import yaml
from yaml.loader import SafeLoader
import json

path = sys.argv[1]

# Open & load the config file into a list
with open('cpd-config.yaml') as f:
    list_doc = yaml.safe_load(f)

# Dict of list of services already installed
serviceInstalled = {
    "parentId" : "cr-service-list",
    "parentTagName": "ul",
    "elementToRender" : "li",
    "data" : []
}

#iterate the state of each instance in the config yaml to get installed services
for x in range(0,len(list_doc["cp4d"][0]["cartridges"])):
    if "state" in list_doc["cp4d"][0]["cartridges"][x] and list_doc["cp4d"][0]["cartridges"][x]["state"]=="installed":
        serviceInstalled["data"].append(list_doc["cp4d"][0]["cartridges"][x]["name"])

# Serializing json
json_object = json.dumps(serviceInstalled, indent=4)
 
# Writing to the json
with open(path, "w") as outfile:
    outfile.write(json_object)
