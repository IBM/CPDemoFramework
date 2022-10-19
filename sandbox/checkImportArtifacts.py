import os.path
import sys

path = sys.argv[1]

import json
import os
import copy

disableImportGovernanceArtifacts = True
numSuccessImportGovernanceArtifacts = 0

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
    sampleJson = copy.deepcopy(templateJson)
    sampleJson["attributes"]["id"] = elementId
    if(action == "disable"):
        sampleJson["attributes"]["classList"]={
            "add": ["hidden-state"]
        }
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


if not os.path.isfile("users.csv"):
    renderData["componentsToRender"][0]["dataToRender"].append(enableDisableArtifactInTimeline("task1","disable"))

if os.path.isfile("governance_artifacts.zip"):
    renderData["componentsToRender"].append(modifyCTA("task2","import-gov-artifacts",";python3.8 importGovArtifacts.py governance_artifacts.zip", numSuccessImportGovernanceArtifacts + 1))
    disableImportGovernanceArtifacts = False


if os.path.isfile("data_protection_rules.json"):
    renderData["componentsToRender"].append(modifyCTA("task2","import-gov-artifacts",";python3.8 importDataProtectionRules.py data_protection_rules.json", numSuccessImportGovernanceArtifacts + 1))
else :
    if(disableImportGovernanceArtifacts):
        renderData["componentsToRender"][0]["dataToRender"].append(enableDisableArtifactInTimeline("task2","disable"))

if not os.path.isfile("project_assets.zip"):
    renderData["componentsToRender"][0]["dataToRender"].append(enableDisableArtifactInTimeline("task3","disable"))

with open(path, "w") as outfile:
    json.dump(renderData, outfile)

print("success")
