import logging
logging.basicConfig(format="%(asctime)s %(levelname)-7s %(message)s", level=logging.INFO)
import pandas
import sys
sys.path.append('../')
import os
from decouple import config
import json
import cpdCLIUtils
import apis

CPD_USER_NAME =  config('WKCUSER')
CPD_USER_PASSWORD =  config('PASSWORD')
CPD_URL = "https://"+config('TZHOSTNAME')
cpdAPIKey = cpdCLIUtils.getAPIKey(CPD_URL, CPD_USER_NAME, CPD_USER_PASSWORD)
os.system('cpd-cli config users set '+ CPD_USER_NAME +' --username '+ CPD_USER_NAME + ' --apikey '+ cpdAPIKey)

os.system('cpd-cli config profiles set sandbox-profile --user '+ CPD_USER_NAME + ' --url '+ CPD_URL)
usersJSON = json.loads(os.popen("cpd-cli user-mgmt list-users --profile sandbox-profile --output json  ").read())


password = ""
for user in usersJSON:
    if "email" not in user:
        user["email"] = '--'
    if user['username']==CPD_USER_NAME:
        user['password']=CPD_USER_PASSWORD
    else:
        user["password"]=password

with open(sys.argv[1], "w") as sys.argv[1]:
    json.dump(usersJSON, sys.argv[1])


#data for group and role management

groupsAPI = apis.endpoints.GroupsAPI()
rolesAPI = apis.endpoints.RolesAPI()


groupsJSON = groupsAPI.getAllGroups()
rolesJSON = rolesAPI.getAllRoles()



with open(sys.argv[2], "w") as sys.argv[2]:
    json.dump(groupsJSON, sys.argv[2])

with open(sys.argv[3], "w") as sys.argv[3]:
    json.dump(rolesJSON, sys.argv[3])

print("success")

