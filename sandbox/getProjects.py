import sys

path = sys.argv[1]

import json
import os
# import platform
# import requests
# import tarfile
# import zipfile
# from IPython.core.display import display, HTML
from decouple import config

path = sys.argv[1]

renderData = {
    "parentId" : "project-list-ul",
    "dataToRender" : []
}
# ## CPD Credentials

# In[2]:
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CPD_USER_NAME =  config('WKCUSER')
CPD_USER_PASSWORD =  config('PASSWORD')
CPD_URL = "https://"+config('TZHOSTNAME')

version_r = os.popen('cpdctl version').read()

CPDCTL_VERSION = version_r
CPDCTL_VERSION=CPDCTL_VERSION.strip()

print("cpdctl version: {}".format(CPDCTL_VERSION))

os.system('cpdctl config user set cpd_user --username '+CPD_USER_NAME+ ' --password '+CPD_USER_PASSWORD)

os.system('cpdctl config profile set cpd --url ' +CPD_URL+' --user cpd_user')

os.system('cpdctl config context set cpd --profile cpd --user cpd_user')

os.system('cpdctl config context list')

os.system('cpdctl config context use cpd')

data = json.loads(os.popen("cpdctl project list --output json").read())
for i in range(0, len(data["resources"])):
    renderData["dataToRender"].append({
        "elementToRender": "li",
        "attributes": {
            "id": "li_"+data['resources'][i]['metadata']['guid'],
            "innerHTML" : data['resources'][i]['entity']['name'],
            "name": data['resources'][i]['metadata']['guid']
        },
        "children": []
    })

print(renderData)
with open(path, "w") as outfile:
    json.dump(renderData, outfile)
print("success")