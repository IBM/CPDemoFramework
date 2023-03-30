import sys
import json

data =  sys.argv[1]

with open("/projects/techzone-demo/olm-utils-v2/data.json", "w") as jsonFile:
    json.dump(json.loads(data), jsonFile)