import yaml
import json

#get list of services
with open('cp4d-services.json') as f:
    cp4d_services = json.load(f)

confg_map_exists = True
try:
    #get the config yaml from config map
    with open('./cpd-config/cp4d-config.yaml') as f:
        config_map_cp4d_yaml = yaml.safe_load(f)
except:
    config_map_exists = False

if(confg_map_exists):
    #check if that service exists in the config map yaml else add it
    for service in cp4d_services:
        if not any(existing_service["name"] == service for existing_service in config_map_cp4d_yaml["cp4d"][0]["cartridges"]):
            config_map_cp4d_yaml["cp4d"][0]["cartridges"].append({"name": service, "state": "removed"})

    #update the default config yaml
    with open("cp4d-config.yaml", "w") as f:
        yaml.dump(config_map_cp4d_yaml, f, sort_keys=False)

    #get the default openshift yaml
    with open('./cpd-config/openshift-config.yaml') as f:
        openshift_yaml = yaml.safe_load(f)

    #update the default openshift yaml
    with open("openshift-config.yaml", "w") as f:
        yaml.dump(openshift_yaml, f, sort_keys=False)
else:
    #get the default config yaml
    with open('cp4d-config.yaml') as f:
        default_cp4d_yaml = yaml.safe_load(f)

    for service in cp4d_services:
        if not any(existing_service["name"] == service for existing_service in default_cp4d_yaml["cp4d"][0]["cartridges"]):
            default_cp4d_yaml["cp4d"][0]["cartridges"].append({"name": service, "state": "removed"})
    
    #update the default config yaml
    with open("cp4d-config.yaml", "w") as f:
        yaml.dump(default_cp4d_yaml, f, sort_keys=False)






