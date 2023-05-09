json=$1
 
readJsonConfig() {
        echo $json | jq -r $1
}

oc_login = $(readJsonConfig ".oc_login")

$oc_login