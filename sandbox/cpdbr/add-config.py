#!/usr/bin/env python
import yaml
from yaml.loader import SafeLoader
from dotenv import dotenv_values
import dotenv

config = dotenv_values(".env") 

#update openshift configuration yaml
with open('dpa.yaml') as f:
    dpa = yaml.safe_load(f)
dpa["spec"]["backupLocations"][0]["velero"]["objectStorage"]["bucket"] = config["BUCKET"]
dpa["spec"]["backupLocations"][0]["velero"]["objectStorage"]["s3Url"] = config["S3_URL"]
dpa["spec"]["backupLocations"][0]["velero"]["config"]["region"] = config["REGION"]
dpa["spec"]["backupLocations"][0]["velero"]["config"]["s3Url"] = config["S3_URL"]
with open("dpa.yaml", "w") as f:
    yaml.dump(dpa, f, sort_keys=False)
