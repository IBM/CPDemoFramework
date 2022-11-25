import logging
logging.basicConfig(format="%(asctime)s %(levelname)-7s %(message)s", level=logging.INFO)
import sys
sys.path.append("../")
import os
import json
from decouple import config
import cpdCLIUtils
import apis

CPD_USER_NAME =  config("WKCUSER")
CPD_USER_PASSWORD =  config("PASSWORD")
CPD_URL = "https://"+config("TZHOSTNAME")
cpdAPIKey = cpdCLIUtils.getAPIKey(CPD_URL, CPD_USER_NAME, CPD_USER_PASSWORD)

usersJSON = open(sys.argv[1], "r")
usersJSON = json.load(usersJSON)

password = sys.argv[2]

userGroupMapping = dict()
keysToRemove = ["created_timestamp","group_roles","groups","last_modified_timestamp","misc"]

for user in usersJSON:
    print(user)
    if user["username"]==CPD_USER_NAME:
        user["password"] = CPD_USER_PASSWORD
    elif str(user["password"]).strip()!="" and not isinstance(user["password"], float):
        pass
    else: 
        user["password"] = password
    for group in user["groups"]:
        if(group["group_id"] != 10000):
            try:
                userGroupMapping[str(group["group_id"])].append(int(user["uid"]))
            except:
                userGroupMapping[str(group["group_id"])] = [int(user["uid"])]
    for key in keysToRemove:
        try:
            del user[key]
        except:
            continue

jsonPath = "usersUpdated.json"
with open(jsonPath, "w") as outfile:
    json.dump(usersJSON, outfile)

print(userGroupMapping)
os.system("cpd-cli config users set "+ CPD_USER_NAME +" --username "+ CPD_USER_NAME + " --apikey "+ cpdAPIKey)

os.system("cpd-cli config profiles set sandbox-profile --user "+ CPD_USER_NAME + " --url "+ CPD_URL)

data = os.popen("cpd-cli user-mgmt bulk-upsert-users --from-json-file "+ jsonPath +" --profile sandbox-profile").read()
print(data)

groupsAPI = apis.endpoints.GroupsAPI()


for group_id in userGroupMapping:
    groupsAPI.getGroupMembers(group_id)
    groupsAPI.addMemberToGroup(group_id,{
        "user_identifiers" : userGroupMapping[group_id]
    })

print("success")