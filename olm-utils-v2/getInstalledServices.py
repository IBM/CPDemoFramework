#!/usr/bin/env python
import sys
import os
import yaml
from yaml.loader import SafeLoader
import json

cpak = sys.argv[1]
path = sys.argv[2]

# Dict of list of services already installed
serviceInstalled = {
    "parentId": "cr-git-services",
    "dataToRender": []
}

############ Hard coded service list ############
services = {
    "analyticsengine": 'Analytics Engine Powered by Apache Spark',
    "bigsql": 'Db2 Big SQL',
    "ca": 'Cognos Analytics',
    "cde": 'Cognos Dashboards',
    "datagate": 'Data Gate',
    "datastage-ent-plus": 'DataStage Enterprise Plus',
    "db2": 'Db2',
    "db2u": 'IBM Db2u',
    "db2wh": 'Db2 Warehouse',
    "dmc": 'Data Management Console',
    "dods": 'Decision Optimization',
    "dp": 'Data Privacy',
    "dv": 'Data Virtualization',
    "hadoop": 'Execution Engine for Apache Hadoop',
    "mdm": 'IBM Master Data Management',
    "openpages": 'OpenPages',
    "planning-analytics": 'Planning Analytics',
    "rstudio": 'RStudio Server',
    "spss": 'SPSS Modeler',
    "voice-gateway": 'Voice Gateway',
    "watson-assistant": 'Watson Assistant',
    "watson-discovery": 'Watson Discovery',
    "watson-ks": 'Watson Knowledge Studio',
    "watson-openscale": 'IBM Watson OpenScale',
    "watson-speech": 'Watson Speech to Text',
    "wkc": 'Watson Knowledge Catalog',
    "wml": 'Watson Machine Learning',
    "wml-accelerator": 'Watson Machine Learning Accelerator',
    "wsl": 'Watson Studio'
}

################################################

#####################For cp4d get the installed services#####################
# Open & load the config file into a list
i=0
if cpak == "cp4d":
    with open('cp4d-config.yaml') as f:
        list_doc = yaml.safe_load(f)
    #iterate the state of each instance in the config yaml to get installed services
    for x in range(0,len(list_doc["cp4d"][0]["cartridges"])):
        #iterate config yaml to get details of the services
        temp = {
                    "elementToRender": "li",
                    "attributes": {
                        "id": ""   #index of li tag
                    },
                    "children": [
                        {
                            "elementToRender": "input",
                            "attributes": {
                                "id": "",   #index of children id tag
                                "value": "",  #value of the service
                                "name": "cr-services",   #name of the service
                                "type": "checkbox",
                                "checked": True       #installed/removed
                            },
                            "children": False
                        },
                        {
                            "elementToRender": "TEXT_NODE",
                            "attributes": {
                                "value": ""     #name of the service
                            },
                            "children": False
                        }
                    ]
                }
        if "state" in list_doc["cp4d"][0]["cartridges"][x]:
            temp["attributes"]["id"] = "li_option"+str(i)
            temp["children"][0]["attributes"]["id"] = "input_option"+str(i)
            temp["children"][0]["attributes"]["value"] = list_doc["cp4d"][0]["cartridges"][x]["name"]
            temp["children"][1]["attributes"]["value"] = services[list_doc["cp4d"][0]["cartridges"][x]["name"]]
            if list_doc["cp4d"][0]["cartridges"][x]["state"] == "installed":
                temp["children"][0]["attributes"]["checked"] = True
            elif list_doc["cp4d"][0]["cartridges"][x]["state"] == "removed":
                temp["children"][0]["attributes"]["checked"] = False
            serviceInstalled["dataToRender"].append(temp)
            i=i+1
#########################################################################

#####################For cp4i get installed services#####################
# Open & load the config file into a list
# elif cpak == "cp4i":
#     with open('cp4i-config.yaml') as f:
#         list_doc = yaml.safe_load(f)
#     #iterate the state of each instance in the config yaml to get installed services
#     for x in range(0,len(list_doc["cp4i"][0]["instances"])):
#         if "state" in list_doc["cp4i"][0]["instances"][x] and list_doc["cp4i"][0]["instances"][x]["state"] == "installed":
#             serviceInstalled["service"].append(list_doc["cp4i"][0]["instances"][x])
#########################################################################

# Serializing json
json_object = json.dumps(serviceInstalled, indent=4)
 
# Writing to the json
with open(path, "w") as outfile:
    outfile.write(json_object)
print("success")
