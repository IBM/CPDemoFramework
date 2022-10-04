oc create namespace oadp-operator
oc patch configs.imageregistry.operator.openshift.io/cluster --type merge -p '{"spec":{"defaultRoute":true}}'
IMAGE_REGISTRY=`oc get route -n openshift-image-registry | grep image-registry | awk '{print $2}'`
NAMESPACE=oadp-operator
CPU_ARCH=`uname -m`
BUILD_NUM=1

# Podman steps (working on removing)

# then oadp installation
oc apply -f oadp-operatorgroup.yaml 
oc apply -f oadp-sub.yaml 

oc annotate namespace oadp-operator openshift.io/node-selector=""

oc create secret generic cloud-credentials --namespace oadp-operator --from-file cloud=./credentials-velero

#pull secret
oc get secret/pull-secret -n openshift-config --template='{{index .data ".dockerconfigjson" | base64decode}}' > source-secret.json
