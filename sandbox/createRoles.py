import logging
logging.basicConfig(format="%(asctime)s %(levelname)-7s %(message)s", level=logging.INFO)
import sys
sys.path.append('../')
from decouple import config
import json
import apis

def createRoles():
    rolesApi = apis.endpoints.RolesAPI()
    existingRoles = rolesApi.getAllRoles()
    roleIdMapping = {}
    with open('roles.json') as outfile:
        data = json.load(outfile)
    newRole = {}
    for role in data["rows"]:   
            filteredRole = list(filter(lambda innerrole:innerrole["doc"]["role_name"] == role["doc"]["role_name"] , existingRoles["rows"]))
            if not filteredRole:
                print("enterd new role")
                newRole["role_name"] = role["doc"]["role_name"]
                newRole['description'] = role["doc"]["description"]
                newRole['permissions'] = role["doc"]["permissions"]
                addRoleResponse = rolesApi.addRole(newRole)
                roleIdMapping[role["id"]] = addRoleResponse["id"]
            else:
                roleIdMapping[role["id"]] = filteredRole[0]["id"]
    return roleIdMapping


