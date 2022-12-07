import logging
logging.basicConfig(format="%(asctime)s %(levelname)-7s %(message)s", level=logging.INFO)
import sys
sys.path.append('../')
from decouple import config
import json
import apis

def createGroups(roleIdMapping):
    groupsApi = apis.endpoints.GroupsAPI()
    existingGroups = groupsApi.getAllGroups()
    groupIdMapping = {}
    print(roleIdMapping)
    with open('groups.json') as outfile:
        data = json.load(outfile)

    newGroup = {}
    for group in data["results"]:  
            filteredGroups = list(filter(lambda innergroup:innergroup["name"] == group["name"] , existingGroups["results"])) 
            if not filteredGroups:
                newGroup["name"] = group["name"]
                newGroup['description'] = group["description"]
                newGroup['role_identifiers'] = []
                #replace role identifiers with newly created roles
                for i in range(len(group['roles'])):
                    if(roleIdMapping.__contains__(group['roles'][i]["role_id"])):
                        newGroup['role_identifiers'].append(roleIdMapping[group['roles'][i]["role_id"]])
                    else:
                        newGroup['role_identifiers'].append(group['roles'][i]["role_id"])
                addGroupResponse = groupsApi.addGroup(newGroup)
                groupIdMapping[group["group_id"]] = addGroupResponse["group_id"]
            else:
                groupIdMapping[group["group_id"]] = filteredGroups[0]["group_id"]
    return groupIdMapping