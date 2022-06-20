#!/usr/bin/env python
# coding: utf-8

# # Train, promote and deploy Boston house prices prediction model

# This notebook contains steps and code to demonstrate support of AI Lifecycle features in Cloud Pak for Data. 
# It contains steps and code to work with [`cpdctl`](https://github.com/IBM/cpdctl) CLI tool available in IBM github repository. 
# It also introduces commands for getting model and training data, persisting model, deploying model
# and promoting it between deployment spaces.
# 
# Some familiarity with Python is helpful. This notebook uses Python 3.7.
# 

# In[1]:


# import base64
import json
import os
# import platform
# import requests
# import tarfile
# import zipfile
# from IPython.core.display import display, HTML
from decouple import config
import sys

# ## CPD Credentials

# In[2]:
#!/usr/bin/python

#Pick the Demo Project and and zip file name from arguments 
###python3.8 importProject.py PROJECT_ZIP DEMO_NAME###

DEMO_NAME=str(sys.argv[2])
PROJECT_ZIP=str(sys.argv[1])+'.zip'
# print(DEMO_NAME)
# print(PROJECT_ZIP)

# print(sys.argv)

### getting credentials from .env file ###
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CPD_USER_NAME =  config("WKCUSER")
CPD_USER_PASSWORD =  config("PASSWORD")
CPD_URL = "https://"+config('TZHOSTNAME')

 
version_r = os.popen('cpdctl version').read()

CPDCTL_VERSION = version_r
CPDCTL_VERSION=CPDCTL_VERSION.split()

print("cpdctl version: {}".format(CPDCTL_VERSION))


# ### Add CPD profile and context configuration

# Add "cpd_user" user to the `cpdctl` configuration

# In[6]:


os.system(' cpdctl config user set cpd_user --username '+CPD_USER_NAME+' --password '+CPD_USER_PASSWORD)


# Add "cpd" profile to the `cpdctl` configuration

# In[7]:


os.system(' cpdctl config profile set cpd --url '+CPD_URL+' --user cpd_user')


# Add "cpd" context to the `cpdctl` configuration

# In[8]:


os.system(' cpdctl config context set cpd --profile cpd --user cpd_user')


# List available contexts

# In[9]:


os.system(' cpdctl config context list')


# In[10]:


os.system(' cpdctl config context use cpd')


JMES_QUERY = "resources[?entity.name == '{}'].metadata.guid".format(DEMO_NAME)
result = os.popen('cpdctl project list --output json --jmes-query "'+JMES_QUERY+'"').read()
PROJECT_IDS = json.loads(result)
if PROJECT_IDS:
    for project_id in PROJECT_IDS:
        print('Deleting project '+DEMO_NAME+'  with ID: {}'.format(project_id))
        os.system('cpdctl project delete --project-id "'+project_id+'"')


os.system('cpdctl project list --output json')

import uuid
STORAGE = {"type": "assetfiles", "guid": str(uuid.uuid4())}
STORAGE_JSON = json.dumps(STORAGE)

result = os.popen('cpdctl project create --name '+DEMO_NAME+' --output json --raw-output --storage \''+STORAGE_JSON+'\' --jmes-query \'location\'').read()
DEMO_PROJECT_ID = result.rsplit('/', 1)[-1]
print("The new '{}' project ID is: {}".format(DEMO_NAME, DEMO_PROJECT_ID))

DEMO_PROJECT_ID=DEMO_PROJECT_ID.strip()
result = os.popen('cpdctl asset import start --project-id '+DEMO_PROJECT_ID+' --import-file '+PROJECT_ZIP+' --output json --jmes-query "metadata.id" --raw-output').read()
IMPORT_ID = result
print("The new import ID is: {}".format(IMPORT_ID))

os.system('cpdctl asset import get --project-id '+DEMO_PROJECT_ID+' --import-id '+IMPORT_ID)

os.system('cpdctl asset search --query \'*:*\' --type-name asset --project-id '+DEMO_PROJECT_ID)

