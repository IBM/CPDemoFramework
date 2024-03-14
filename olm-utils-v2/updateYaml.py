#!/usr/bin/env python
import sys
import base64
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


# update cp4waiops configuration yaml
elif cpak.lower()=='cp4waiops':
    
    # cp4waiops licences handling
    if (len(sys.argv) > 4):
        instana_saleskey=sys.argv[5]
        instana_agentkey=sys.argv[6]
        turbo_lic=sys.argv[7]
        turbo_lic = base64.b64decode(turbo_lic.encode('ascii')).decode('ascii')

    with open('cp4waiops-config.yaml') as f:
        list_cp4waiops = yaml.safe_load(f)
        
    for project in range(0,len(list_cp4waiops['cp4waiops'])):
        for all_services in range(0,len(list_cp4waiops["cp4waiops"][project]["instances"])):
            if "install" in list_cp4waiops["cp4waiops"][project]["instances"][all_services]:
                list_cp4waiops["cp4waiops"][project]["instances"][all_services]["install"] = bool('')
                #print(list_cp4waiops["cp4waiops"][project]["instances"][all_services])
            for selected_service in range(0,len(component_list)):
                if list_cp4waiops["cp4waiops"][project]["instances"][all_services]["kind"] == component_list[selected_service]:
                    list_cp4waiops["cp4waiops"][project]["instances"][all_services]["install"] = bool('true')
                    print(list_cp4waiops["cp4waiops"][project]["instances"][all_services])
                    ## Update Licenses for cp4waiops services (Instana, Turbonomic) ##
                    if list_cp4waiops["cp4waiops"][project]["instances"][all_services]['name'] == "cp4waiops-instana":
                        if((instana_agentkey) and (instana_saleskey)):
                            list_cp4waiops["cp4waiops"][project]["instances"][all_services]["sales_key"]= instana_saleskey
                            list_cp4waiops["cp4waiops"][project]["instances"][all_services]["agent_key"]= instana_agentkey
                            
                    if list_cp4waiops["cp4waiops"][project]["instances"][all_services]['name'] == "cp4waiops-turbonomic":
                        if(turbo_lic):
                            list_cp4waiops["cp4waiops"][project]["instances"][all_services]["turbo_license"]= turbo_lic

    with open("cp4waiops-config.yaml", "w") as f:
        yaml.dump(list_cp4waiops, f, sort_keys=False)

# update cp4ba configuration yaml
elif cpak.lower()=='cp4ba':

    with open('cp4ba-config.yaml') as f:
        list_cp4ba = yaml.safe_load(f)

    cp4ba_main = {'decisions','decisions_ads','content','application','document_processing','workflow','pm','rpa'}
    cp4ba_additionals = ['cloudbeaver_enabled','roundcube_enabled','cerebro_enabled','akhq_enabled','mongo_express_enabled','phpldapadmin_enabled']
    cp4ba_optional_components = {'foundation':['bas','bai','ae'],'decisions':['decision_center','decision_runner','decision_server_runtime'],'decisions_ads':['ads_designer','ads_runtime'],'content':['cmis','css','es','tm','ier'],'application':['app_designer','ae_data_persistence'],'document_processing':['document_processing_designer'],'workflow':['baw_authoring','kafka']}

    # Reset all to false
    ## main
    for component in cp4ba_main:
        if component == "pm":
            list_cp4ba['cp4ba'][0]['pm']['enabled'] = bool('')
        elif component == "rpa":
            list_cp4ba['cp4ba'][0]['rpa']['enabled'] = bool('')
        else:
            list_cp4ba['cp4ba'][0]['cp4ba']['patterns'][component]['enabled'] = bool('')

    ## additionals
    for component in cp4ba_additionals:
        list_cp4ba['cp4ba'][0][component] = bool('')


    ## optional components (only for cp4ba patterns)
    for component in cp4ba_optional_components:
        for every_optcomp in cp4ba_optional_components[component]:
            list_cp4ba['cp4ba'][0]['cp4ba']['patterns'][component]['optional_components'][every_optcomp] = bool('')

    # Set selections as per component list
    ## main
    for component in component_list:
        if component in cp4ba_main:
            if component == "pm":
                list_cp4ba['cp4ba'][0]['pm']['enabled'] = bool('true')
            elif component == "rpa":
                list_cp4ba['cp4ba'][0]['rpa']['enabled'] = bool('true')
            else:
                list_cp4ba['cp4ba'][0]['cp4ba']['patterns'][component]['enabled'] = bool('true')

    ## additionals
    for component in component_list:
        if component in cp4ba_additionals:
            list_cp4ba['cp4ba'][0][component] = bool('true')


    ## optional components (only for cp4ba patterns)
    for component in component_list:
        if component in cp4ba_optional_components and cp4ba_optional_components[component]:
            for every_optcomp in cp4ba_optional_components[component]:
                if every_optcomp in component_list:
                    list_cp4ba['cp4ba'][0]['cp4ba']['patterns'][component]['optional_components'][every_optcomp] = bool('true')


    with open('cp4ba-config.yaml',"w") as f:
        yaml.dump(list_cp4ba, f, sort_keys=False)


print("success")
