import sys

path = sys.argv[1]

import json
 
# Data to be written
dictionary = {
    "parentId" : "project-list",
    "parentTagName": "ul",
    "elementToRender" : "li",
    "data" : ["Project 1", "Project 2", "Project 3","Project 4"]
}
 
with open(path, "w") as outfile:
    json.dump(dictionary, outfile)