oc create namespace oadp-operator
oc patch configs.imageregistry.operator.openshift.io/cluster --type merge -p '{"spec":{"defaultRoute":true}}'
IMAGE_REGISTRY=`oc get route -n openshift-image-registry | grep image-registry | awk '{print $2}'`
NAMESPACE=oadp-operator
CPU_ARCH=`uname -m`
BUILD_NUM=1
