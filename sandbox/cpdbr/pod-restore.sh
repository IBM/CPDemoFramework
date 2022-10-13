CPD_INSTANCE=$1
CPD_INSTANCE_BACKUP=$2
CPD_OPERATOR_BACKUP=$3

echo "Restoring CPD operators..."

cpd-cli oadp client config set namespace=oadp-operator
wget https://raw.githubusercontent.com/IBM/cpd-cli/master/cpdops/files/cpd-operators.sh
chmod +x cpd-operators.sh
cpd-cli oadp restore create --from-backup=${CPD_OPERATOR_BACKUP} operator-restore1-${CPD_OPERATOR_BACKUP} --include-resources='crd' --include-cluster-resources=true --skip-hooks --log-level=debug --verbose
cpd-cli oadp restore create --from-backup=${CPD_OPERATOR_BACKUP} operator-restore2-${CPD_OPERATOR_BACKUP} --include-resources='namespaces,operatorgroups,scheduling,crd' --include-cluster-resources=true --skip-hooks --log-level=debug --verbose
cpd-cli oadp restore create --from-backup=${CPD_OPERATOR_BACKUP} operator-restore3-${CPD_OPERATOR_BACKUP} --include-resources='configmaps' --selector 'app=cpd-operators-backup' --skip-hooks --log-level=debug --verbose
./cpd-operators.sh restore --foundation-namespace ibm-common-services --operators-namespace ibm-common-services
oc patch NamespaceScope common-service -n ibm-common-services --type=merge --patch='{"spec": {"csvInjector": {"enable": true} } }'


echo "Restoring CPD instance..."
cpd-cli oadp restore create --from-backup=${CPD_INSTANCE_BACKUP} --include-resources='namespaces,zenservices,secrets,certificates.cert-manager.io,certificates.certmanager.k8s.io,issuers.cert-manager.io,issuers.certmanager.k8s.io' ${CPD_INSTANCE_BACKUP}-zenservice-restore --skip-hooks --log-level=debug --verbose
cpd-cli oadp restore create --from-backup=${CPD_INSTANCE_BACKUP} --exclude-resources='clients,ImageTag' ${CPD_INSTANCE_BACKUP}-restore --include-cluster-resources=true --log-level=debug --verbose
