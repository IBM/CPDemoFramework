import yaml
import sys
import os

def load_yaml_file(file_path):
    with open(file_path) as file_content:
        return yaml.safe_load(file_content)

def generate_config_yaml(config_data, file_path):
    with open(file_path, "w") as file_content:
        yaml.dump(config_data, file_content, sort_keys=False)

def services_dict_without_description(cpak, default_config_yaml):
    services = {}
    if(cpak == "cp4d"):
        for service in default_config_yaml["cp4d"][0]["cartridges"]:
                try:
                    del service["description"]
                    services[service["name"]] = service
                except:
                    pass
    elif(cpak == "cp4i"):
        pass
    elif(cpak == "cp4waiops"):
        for project in range(0,len(default_config_yaml["cp4waiops"])):
            for service in range(0,len(default_config_yaml["cp4waiops"][project]["instances"])):        
                try:
                    del default_config_yaml["cp4waiops"][project]["instances"][service]['description']
                    services[default_config_yaml["cp4waiops"][project]["instances"][service]['kind']] = default_config_yaml["cp4waiops"][project]["instances"][service]
                except:
                    pass

    return services

def services_project_association(cpak, default_config_yaml):
    service_project_map = {}
    
    cpak_config = {"cp4d":['cp4d','cartridges','name'],
                   "cp4i":['cp4i','instances','type'],
                   "cp4waiops":['cp4waiops','instances','kind']}

    for projectidx,project in enumerate(default_config_yaml[cpak_config[cpak][0]]):
        servicelist = []
        for _,sv in enumerate(project[cpak_config[cpak][1]]):
            servicelist.append(sv[cpak_config[cpak][2]])

        servicelist.append(projectidx)
        service_project_map[project['project']] = servicelist

    return service_project_map

def compareAndMergeYaml(cpak,services_dict,config_map_yaml,service_project_map):
    if(cpak == "cp4d"):
        for service in services_dict:
            if not any(existing_service["name"] == service for existing_service in config_map_yaml["cp4d"][0]["cartridges"]):
                config_map_yaml["cp4d"][0]["cartridges"].append(services_dict[service])
    elif(cpak == "cp4i"):
        pass
    elif(cpak == "cp4waiops"):
        for service in services_dict:
            if not any (service == config['kind'] for _,project in enumerate(config_map_yaml["cp4waiops"]) for _,config in enumerate(project['instances'])):
                for projectitem in service_project_map:
                    if service in service_project_map[projectitem]:
                        config_map_yaml["cp4waiops"][service_project_map[projectitem][-1]]["instances"].append(services_dict[service])

    return config_map_yaml

try:
    cpak = sys.argv[1]
    config_map_exists = os.path.isfile(cpak + "-config.yaml")
    default_config_yaml = load_yaml_file("default-" + cpak + "-config.yaml")
    services_dict = services_dict_without_description(cpak, default_config_yaml)

    if(config_map_exists):
        config_map_yaml = load_yaml_file(cpak + "-config.yaml")
        service_map = services_project_association(cpak, default_config_yaml)
        config_data = compareAndMergeYaml(cpak,services_dict, config_map_yaml,service_map)
    else:
        config_data = default_config_yaml

    generate_config_yaml(config_data, cpak + "-config.yaml")
except:
    pass