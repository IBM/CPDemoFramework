import yaml
import json
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
        pass
    return services

def compareAndMergeYaml(cpak, default_config_yaml, config_map_yaml):
    if(cpak == "cp4d"):
        for service in services_dict:
            if not any(existing_service["name"] == service for existing_service in config_map_yaml["cp4d"][0]["cartridges"]):
                config_map_yaml["cp4d"][0]["cartridges"].append(services_dict[service])
    elif(cpak == "cp4i"):
        pass
    elif(cpak == "cp4waiops"):
        pass
    return config_map_yaml

try:
    cpak = sys.argv[1]
    config_map_exists = os.path.isfile(cpak + "-config.yaml")
    default_config_yaml = load_yaml_file("default-" + cpak + "-config.yaml")
    services_dict = services_dict_without_description(cpak, default_config_yaml)

    if(config_map_exists):
        config_map_yaml = load_yaml_file(cpak + "-config.yaml")
        config_data = compareAndMergeYaml(cpak, default_config_yaml, config_map_yaml)
    else:
        config_data = default_config_yaml

    generate_config_yaml(config_data, cpak + "-config.yaml")
except:
    pass