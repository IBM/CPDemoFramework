import os.path
import sys

path = sys.argv[1]

import json
import os
import copy


disableImportGovernanceArtifacts = True
numSuccessImportGovernanceArtifacts = 0
availableArifacts = 3

metaData = open("readme.json", "r")
metaData = json.load(metaData)


renderData = {
    "componentsToRender" : [
        {
             "parentId" : "timeline-container",
             "dataToRender" : []
        }
    ]
}

templateJson = {
    "elementToRender": "div",
    "attributes": {
        "id": "",
        "classList": {}
    },
    "children" : []
}

modifyCTAJSON = {
    "parentId":"",
    "dataToRender": [
        {
            "elementToRender": "button",
            "attributes": {
                "id" : "",
            },
            "children": []
        }
    ]
}

def enableDisableArtifactInTimeline(elementId, action):
    global availableArifacts
    sampleJson = copy.deepcopy(templateJson)
    sampleJson["attributes"]["id"] = elementId
    if(action == "disable"):
        sampleJson["attributes"]["classList"]={
            "add": ["hidden-state"]
        }
        availableArifacts = availableArifacts - 1
    elif(action == "enable"):
         sampleJson["attributes"]["classList"]={
            "remove": ["hidden-state"]
        }
    return sampleJson

def modifyCTA(parentId, elementId, command, numSuccess):
     sampleJson = copy.deepcopy(modifyCTAJSON)
     sampleJson["parentId"] = parentId
     sampleJson["dataToRender"][0]["attributes"]["id"] = elementId
     sampleJson["dataToRender"][0]["attributes"]["command"] = command
     sampleJson["dataToRender"][0]["attributes"]["numSuccess"] = numSuccess
     return sampleJson

def modifyContent(parentId,elements):
    sampleJson = dict({"parentId" : parentId, "dataToRender": []})
    for element in elements:
        sampleJson["dataToRender"].append(element)
    return sampleJson

if "version" not in metaData or ("version" in metaData and metaData["version"] == 1.0):
    if not os.path.isfile("users.csv"):
        renderData["componentsToRender"][0]["dataToRender"].append(enableDisableArtifactInTimeline("task1","disable"))
    else:
        renderData["componentsToRender"].append(modifyCTA("task1","create-users",";python3.8 createUsers.py users.csv {IMPORT_USERS_PASSWORD}", 1))
        renderData["componentsToRender"].append(modifyContent("create-users-content", [
            {
                "elementToRender": "p",
                "attributes": {
                        "id" : "create-users-content-line1",
                        "textContent" : "User management"
                    },
                "children": []
            },
            {
                "elementToRender": "p",
                "attributes": {
                        "id" : "create-users-content-line2",
                        "textContent" : "Recreate demo users onto new CP4D cluster."
                    },
                "children": []
            }
        ]))

if "version" in metaData and metaData["version"] == 2.0:
    if not os.path.isfile("users.json"):
        renderData["componentsToRender"][0]["dataToRender"].append(enableDisableArtifactInTimeline("task1","disable"))
    else:
        renderData["componentsToRender"].append(modifyCTA("task1","create-users",";python3.8 createUsersv2.py users.json {IMPORT_USERS_PASSWORD}", 1))

if os.path.isfile("governance_artifacts.zip"):
    numSuccessImportGovernanceArtifacts = numSuccessImportGovernanceArtifacts + 1
    renderData["componentsToRender"].append(modifyCTA("task2","import-gov-artifacts",";python3.8 importGovArtifacts.py governance_artifacts.zip", numSuccessImportGovernanceArtifacts))
    disableImportGovernanceArtifacts = False


if os.path.isfile("data_protection_rules.json"):
    numSuccessImportGovernanceArtifacts = numSuccessImportGovernanceArtifacts + 1
    renderData["componentsToRender"].append(modifyCTA("task2","import-gov-artifacts",";python3.8 importDataProtectionRules.py data_protection_rules.json", numSuccessImportGovernanceArtifacts))
else :
    if(disableImportGovernanceArtifacts):
        renderData["componentsToRender"][0]["dataToRender"].append(enableDisableArtifactInTimeline("task2","disable"))

if not os.path.isfile("project_assets.zip"):
    renderData["componentsToRender"][0]["dataToRender"].append(enableDisableArtifactInTimeline("task3","disable"))

if(availableArifacts == 0):
    renderData["componentsToRender"].append({
        "parentId":"artifact-message-div",
        "dataToRender": [
        {
            "elementToRender": "p",
            "attributes": {
                "id" : "artifact-message",
                "textContent" : "No artifacts are available for import."
            },
            "children": []
        }
    ]
    })

with open(path, "w") as outfile:
    json.dump(renderData, outfile)

print("success")
