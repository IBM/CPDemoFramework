oc create namespace oadp-operator
oc annotate namespace oadp-operator openshift.io/node-selector=""
oc create secret generic cloud-credentials --namespace oadp-operator --from-file cloud=./credentials-velero.txt
oc apply -f oadp-operatorgroup.yaml
oc apply -f oadp-sub.yaml
oc create -f dpa.yaml -n oadp-operator
cpd-cli oadp client config set namespace=oadp-operator
cpd-cli oadp client config set cpd-namespace=cpd-instance

#pull secret
oc get secret/pull-secret -n openshift-config --template='{{index .data ".dockerconfigjson" | base64decode}}' > source-secret.json
