#!/usr/bin/env python
import sys
import os
import yaml
from yaml.loader import SafeLoader
import json

cpak = sys.argv[1]
path = sys.argv[2]
cp4d_version = "4.7.0"
cp4i_version = "2022.4.1-0"

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
    with open('default-cp4d-config.yaml') as f:
        default_cp4d_yaml = yaml.safe_load(f)

    servicescp4d = {}
    for service in default_cp4d_yaml["cp4d"][0]["cartridges"]:
        try:
            servicescp4d[service["name"]] = service["description"]
        except:
            pass
    
    
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
            try:
                temp["children"][1]["attributes"]["value"] = servicescp4d[list_doc["cp4d"][0]["cartridges"][x]["name"]]
            except:
                temp["children"][1]["attributes"]["value"] = list_doc["cp4d"][0]["cartridges"][x]["name"]
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
    with open('default-cp4i-config.yaml') as f:
        default_cp4d_yaml = yaml.safe_load(f)

    servicescp4i = {}
    for service in default_cp4d_yaml["cp4i"][0]["instances"]:
        try:
            servicescp4i[service["type"]] = service["description"]
        except:
            pass
            
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
            try:
                temp["children"][1]["attributes"]["value"] = servicescp4i[list_doc["cp4i"][0]["instances"][x]["type"]]
            except:
                temp["children"][1]["attributes"]["value"] = list_doc["cp4i"][0]["instances"][x]["type"]
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


#####################For cp4waiops get the installed services#####################
i=0
if cpak == "cp4waiops":

    # service list generation
    with open('default-cp4waiops-config.yaml') as f:
        default_cp4waiops_yaml = yaml.safe_load(f)

    servicescp4waiops = {}
    for project in range(0,len(default_cp4waiops_yaml["cp4waiops"])):
        for service in range(0,len(default_cp4waiops_yaml["cp4waiops"][project]["instances"])):        
            try:
                servicescp4waiops[default_cp4waiops_yaml["cp4waiops"][project]["instances"][service]['kind']] = default_cp4waiops_yaml["cp4waiops"][project]["instances"][service]['description']
            except:
                pass

    serviceversionscp4waiops = {
    "AIManager": 'subscription_channel',
    "AIManagerDemoContent": '',
    "EventManager": 'noi_version',
    "ELK": '',
    "Instana": '',
    "Turbonomic": 'turbo_version',
    "TurbonomicDemoContent": ''
    }

    # Open & load the config file into a list
    with open('cp4waiops-config.yaml') as f:
        list_doc = yaml.safe_load(f)
    #iterate the state of each instance in the config yaml to get installed services
    servicename=''
    ver=''
    for project in range(0,len(list_doc["cp4waiops"])):
        for all_services in range(0,len(list_doc["cp4waiops"][project]["instances"])):
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


            # versions updation
            servicename = list_doc["cp4waiops"][project]["instances"][all_services]["kind"]
            if(serviceversionscp4waiops[servicename]): 
                ver = " ("+str(list_doc["cp4waiops"][project]["instances"][all_services][serviceversionscp4waiops[servicename]])+")"
            else: ver = ""
            servicescp4waiops[servicename]+=ver

            if "install" in list_doc["cp4waiops"][project]["instances"][all_services]:
                servicename = list_doc["cp4waiops"][project]["instances"][all_services]["kind"]
                temp["attributes"]["id"] = "li_option"+servicename
                temp["children"][0]["attributes"]["id"] = "input_option"+servicename
                temp["children"][0]["attributes"]["value"] = servicename
                temp["children"][1]["attributes"]["value"] = servicescp4waiops[servicename]
                if list_doc["cp4waiops"][project]["instances"][all_services]["install"] == bool('true'):
                    temp["children"][0]["attributes"]["checked"] = True
                elif list_doc["cp4waiops"][project]["instances"][all_services]["install"] == bool(''):
                    temp["children"][0]["attributes"]["checked"] = False
                serviceInstalled["componentsToRender"][0]["dataToRender"].append(temp)
                i=i+1

#########################################################################


#####################For cp4ba get the installed services#####################
i=0
if cpak == "cp4ba":
    
    with open('cp4ba-config.yaml') as f:
        cp4ba_yaml = yaml.safe_load(f)

    cp4ba_main = {'decisions','decisions_ads','content','application','document_processing','workflow','pm','rpa'}
    cp4ba_additionals = ['cloudbeaver_enabled','roundcube_enabled','cerebro_enabled','akhq_enabled','mongo_express_enabled']
    cp4ba_optional_components = {'foundation':['bas','bai','ae'],'decisions':['decision_center','decision_runner','decision_server_runtime'],'decisions_ads':['ads_designer','ads_runtime'],'content':['cmis','css','es','tm','ier'],'application':['app_designer','ae_data_persistence'],'document_processing':['document_processing_designer'],'workflow':['baw_authoring']}


    installed_services_list = []

    ## main
    for component in cp4ba_main:
        if component == "pm":
            if cp4ba_yaml['cp4ba'][0]['pm']['enabled']:
                installed_services_list.append('pm')
        elif component == "rpa":
            if cp4ba_yaml['cp4ba'][0]['rpa']['enabled']:
                installed_services_list.append('rpa')
        else:
            if cp4ba_yaml['cp4ba'][0]['cp4ba']['patterns'][component]['enabled']:
                installed_services_list.append(component)


    ## additionals
    for component in cp4ba_additionals:
        if cp4ba_yaml['cp4ba'][0][component]:
            installed_services_list.append(component)


    ## optional components (only for cp4ba patterns)
    for optional_comp in cp4ba_optional_components:
        for each_optional_comp in cp4ba_optional_components[optional_comp]:
            if cp4ba_yaml['cp4ba'][0]['cp4ba']['patterns'][optional_comp]['optional_components'][each_optional_comp]:
                installed_services_list.append(each_optional_comp)


    serviceInstalled = [] # unused
    
    # print(installed_services_list)

    # Serializing json
    json_object = json.dumps(installed_services_list)

    # Writing to the json file
    with open("./installed_cp4ba_services.json", "w+") as service_list_file:
        service_list_file.write(json_object)
    


#########################################################################

if path:
    # Serializing json
    json_object = json.dumps(serviceInstalled, indent=4)

    # Writing to the json
    with open(path, "w") as outfile:
        outfile.write(json_object)
    print("success")
