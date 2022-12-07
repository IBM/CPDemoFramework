#!/usr/bin/env python
import sys
import os
import yaml
from yaml.loader import SafeLoader
import json

cpak = sys.argv[1]
path = sys.argv[2]
cp4d_version = "4.5.1"
cp4i_version = "2022.2.1-0"

# Dict of list of services already installed
serviceInstalled = {
    "componentsToRender" : [
        {
            "parentId": "git-services",
            "dataToRender": []
        }
    ]
}

#####################For cp4d get the installed services#####################

i=0
if cpak == "cp4d":
    ############ Hard coded service list ############
    servicescp4d = {
        "analyticsengine": 'Analytics Engine Powered by Apache Spark',
        "bigsql": 'Db2 Big SQL',
        "ca": 'Cognos Analytics',
        "cde": 'Cognos Dashboards',
        "datagate": 'Data Gate',
        "datastage-ent-plus": 'DataStage Enterprise Plus',
        "db2": 'Db2',
        "db2wh": 'Db2 Warehouse',
        "dmc": 'Data Management Console',
        "dods": 'Decision Optimization',
        "dp": 'Data Privacy',
        "dv": 'Data Virtualization',
        "factsheet": 'AI Factsheets',
        "hadoop": 'Execution Engine for Apache Hadoop',
        "match360": 'Match360',
        "openpages": 'OpenPages',
        "planning-analytics": 'Planning Analytics',
        "replication": 'Data Replication',
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
        "ws-pipelines": 'Watson Studio Pipelines',
        "wsl": 'Watson Studio'
    }
    # Open & load the config file into a list
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
                                "class" : "store-data",
                                "name": "services",   #name of the service
                                "type": "checkbox",
                                "checked": True,       #installed/removed
                                "addEventListener" : ["change","updateSelectedServices"],
                                "dispatchEvent" : "change"
                            },
                            "children": []
                        },
                        {
                            "elementToRender": "TEXT_NODE",
                            "attributes": {
                                "value": ""     #name of the service
                            },
                            "children": []
                        }
                    ]
                }
        if "state" in list_doc["cp4d"][0]["cartridges"][x]:
            temp["attributes"]["id"] = "li_option"+list_doc["cp4d"][0]["cartridges"][x]["name"]
            temp["children"][0]["attributes"]["id"] = "input_option"+list_doc["cp4d"][0]["cartridges"][x]["name"]
            temp["children"][0]["attributes"]["value"] = list_doc["cp4d"][0]["cartridges"][x]["name"]
            temp["children"][1]["attributes"]["value"] = servicescp4d[list_doc["cp4d"][0]["cartridges"][x]["name"]]
            if list_doc["cp4d"][0]["cartridges"][x]["state"] == "installed":
                temp["children"][0]["attributes"]["checked"] = True
            elif list_doc["cp4d"][0]["cartridges"][x]["state"] == "removed":
                temp["children"][0]["attributes"]["checked"] = False
            serviceInstalled["componentsToRender"][0]["dataToRender"].append(temp)
            i=i+1
    try:
        cp4d_version = list_doc["cp4d"][0]["cp4d_version"]
    except:
        pass
    serviceInstalled["componentsToRender"].append({
        "parentId":"cp4d-deploy",
        "dataToRender":[
            {
                "elementToRender": "input",
                "attributes": {
                    "id": "cp4d_version",
                    "value": cp4d_version
                },
                "children": []
            }
        ]
    })
#########################################################################

#####################For cp4i get installed services#####################

i=0
if cpak == "cp4i":
    ############ Hard coded service list ############
    servicescp4i = {
        "platform-navigator": "Platform Navigator",
        "api-management": "API Management",
        "automation-assets": "Automation Assets",
        "enterprise-gateway": "Enterprise Gateway",
        "event-endpoint-management": "Event Endpoint Management",
        "event-streams": "Event Steam",
        "high-speed-transfer-server": "High Speed Transfer Server",
        "integration-dashboard": "Integration Dashboard",
        "integration-design": "Integration Design",
        "integration-tracing": "Integration tracing",
        "messaging": "Messaging"
    }
    # Open & load the config file into a list
    with open('cp4i-config.yaml') as f:
        list_doc = yaml.safe_load(f)
    #iterate the state of each instance in the config yaml to get installed services
    for x in range(0,len(list_doc["cp4i"][0]["instances"])):
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
                                "class": "store-data",
                                "value": "",  #value of the service
                                "name": "services",   #name of the service
                                "type": "checkbox",
                                "checked": True,      #installed/removed
                                "addEventListener" : ["change","updateSelectedServices"],
                                "dispatchEvent" : "change"
                            },
                            "children": []
                        },
                        {
                            "elementToRender": "TEXT_NODE",
                            "attributes": {
                                "value": ""     #name of the service
                            },
                            "children": []
                        }
                    ]
                }
        if "state" in list_doc["cp4i"][0]["instances"][x]:
            temp["attributes"]["id"] = "li_option"+list_doc["cp4i"][0]["instances"][x]["type"]
            temp["children"][0]["attributes"]["id"] = "input_option"+list_doc["cp4i"][0]["instances"][x]["type"]
            temp["children"][0]["attributes"]["value"] = list_doc["cp4i"][0]["instances"][x]["type"]
            temp["children"][1]["attributes"]["value"] = servicescp4i[list_doc["cp4i"][0]["instances"][x]["type"]]
            if list_doc["cp4i"][0]["instances"][x]["state"] == "installed":
                temp["children"][0]["attributes"]["checked"] = True
            elif list_doc["cp4i"][0]["instances"][x]["state"] == "removed":
                temp["children"][0]["attributes"]["checked"] = False
            serviceInstalled["componentsToRender"][0]["dataToRender"].append(temp)
            i=i+1
    try:
        cp4i_version = list_doc["cp4i"][0]["cp4i_version"]
    except:
        pass
    serviceInstalled["componentsToRender"].append({
        "parentId":"cp4i-deploy",
        "dataToRender":[
            {
                "elementToRender": "input",
                "attributes": {
                    "id": "cp4i_version",
                    "value": cp4i_version
                },
                "children": []
            }
        ]
    })
#########################################################################

# Serializing json
json_object = json.dumps(serviceInstalled, indent=4)
 
# Writing to the json
with open(path, "w") as outfile:
    outfile.write(json_object)
print("success")
