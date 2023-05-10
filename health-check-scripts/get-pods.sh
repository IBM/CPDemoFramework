json=$1
 
readJsonConfig() {
        echo $json | jq -r $1
}

$(readJsonConfig ".oc_login")
oc project $(readJsonConfig ".project_name")
oc get pods