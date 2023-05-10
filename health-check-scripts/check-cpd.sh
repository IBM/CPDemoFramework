json=$1
 
readJsonConfig() {
        echo $json | jq -r $1
}

$(readJsonConfig ".oc_login")

oc get "project/cpd" > /dev/null 2>&1

if [ "$?" == "0" ]; then
    echo "CP4D is installed!"
    exit 0
fi

echo "CP4D installation not found"
