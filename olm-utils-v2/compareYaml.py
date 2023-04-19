import yaml

#get the default config yaml
with open('cp4d-config.yaml') as f:
    default_cp4d_yaml = yaml.safe_load(f)

#get the config yaml from config map
with open('./cpd-config/cp4d-config.yaml') as f:
    config_map_cp4d_yaml = yaml.safe_load(f)


#check if that service exists in the config map yaml else add it
for i in range(len(default_cp4d_yaml["cp4d"][0]["cartridges"])):
    if not any(existing_service["name"] == default_cp4d_yaml["cp4d"][0]["cartridges"][i]["name"] for existing_service in config_map_cp4d_yaml["cp4d"][0]["cartridges"]):
        config_map_cp4d_yaml["cp4d"][0]["cartridges"].append({"name": default_cp4d_yaml["cp4d"][0]["cartridges"][i]["name"], "state": "removed"})

#update the default config yaml
with open("cp4d-config.yaml", "w") as f:
    yaml.dump(config_map_cp4d_yaml, f, sort_keys=False)

#get the default openshift yaml
with open('./cpd-config/openshift-config.yaml') as f:
    openshift_yaml = yaml.safe_load(f)

#update the default openshift yaml
with open("openshift-config.yaml", "w") as f:
    yaml.dump(openshift_yaml, f, sort_keys=False)







