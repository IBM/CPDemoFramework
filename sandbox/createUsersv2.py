import logging
logging.basicConfig(format="%(asctime)s %(levelname)-7s %(message)s", level=logging.INFO)
import sys
sys.path.append("../")
import os
import json
from decouple import config
import cpdCLIUtils
import apis
import createGroups
import createRoles

CPD_USER_NAME =  config("WKCUSER")
CPD_USER_PASSWORD =  config("PASSWORD")
CPD_URL = "https://"+config("TZHOSTNAME")
cpdAPIKey = cpdCLIUtils.getAPIKey(CPD_URL, CPD_USER_NAME, CPD_USER_PASSWORD)
rolesMapping = createRoles.createRoles()
groupsMapping = createGroups.createGroups(rolesMapping)

#load users from json
usersJSON = open(sys.argv[1], "r")
usersJSON = json.load(usersJSON)

password = sys.argv[2]

userGroupMapping = dict()
usersMapping = dict()
keysToRemove = ["created_timestamp","group_roles","groups","last_modified_timestamp","misc"]

for user in usersJSON:
    if user["username"]==CPD_USER_NAME:
        user["password"] = CPD_USER_PASSWORD
    elif str(user["password"]).strip()!="" and not isinstance(user["password"], float):
        pass
    else: 
        user["password"] = password
    #to keep track of old group_id and new group_id
    for group in user["groups"]:
        if(group["group_id"] != 10000):
            try:
                userGroupMapping[group["group_id"]].append(user["username"])
            except:
                userGroupMapping[group["group_id"]] = [user["username"]]
    for i in range(len(user['user_roles'])):
        # replace existing role with new role
        user['user_roles'][i] = rolesMapping[user['user_roles'][i]]
    #to keep track of old user_id and new user_id
    usersMapping[user["username"]] = str(user["uid"])

    for key in keysToRemove:
            try:
                del user[key]
            except:
                continue

jsonPath = "usersUpdated.json"
with open(jsonPath, "w") as outfile:
    json.dump(usersJSON, outfile)

os.system("cpd-cli config users set "+ CPD_USER_NAME +" --username "+ CPD_USER_NAME + " --apikey "+ cpdAPIKey)

os.system("cpd-cli config profiles set sandbox-profile --user "+ CPD_USER_NAME + " --url "+ CPD_URL)

data = os.popen("cpd-cli user-mgmt bulk-upsert-users --from-json-file "+ jsonPath +" --profile sandbox-profile --verbose").read()

usersJSON = json.loads(os.popen("cpd-cli user-mgmt list-users --profile sandbox-profile --output json").read())

#update new user_ids
for user in usersJSON:
    usersMapping[user["username"]] = int(user["uid"])

newUserGroupMapping = dict()

#create user and group mapping with updated group_id and user_id
for group in userGroupMapping:
    for user in userGroupMapping[group]:
        if(group != 10000):
            try:
                newUserGroupMapping[str(groupsMapping[group])].append(usersMapping[user])
            except:
                newUserGroupMapping[str(groupsMapping[group])] = [usersMapping[user]]

groupsAPI = apis.endpoints.GroupsAPI()
    
for group_id in newUserGroupMapping:
    groupsAPI.addMemberToGroup(group_id,{
        "user_identifiers" : newUserGroupMapping[group_id]
    })

print("success")