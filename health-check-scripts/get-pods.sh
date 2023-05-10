json=$1
 
readJsonConfig() {
        echo $json | jq -r $1
}

$(readJsonConfig ".oc_login")
project_name=$(readJsonConfig ".project_name")
oc project $project_name
oc get pods