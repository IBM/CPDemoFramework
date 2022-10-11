CPD_INSTANCE=$1
CPD_INSTANCE_BACKUP=$2
CPD_OPERATOR_BACKUP=$3
echo "Backing up CPD instance..."
cpd-cli oadp backup create --include-namespaces=${CPD_INSTANCE} --exclude-resources='Event,Event.events.k8s.io' --default-volumes-to-restic --snapshot-volumes=false --cleanup-completed-resources ${CPD_INSTANCE_BACKUP} --log-level=debug --verbose

echo "Backing up CPD operators.."
cpd-cli oadp client config set cpd-namespace=${CPD_INSTANCE}
wget https://raw.githubusercontent.com/IBM/cpd-cli/master/cpdops/files/cpd-operators.sh
chmod +x cpd-operators.sh
./cpd-operators.sh backup --foundation-namespace ibm-common-services --operators-namespace ibm-common-services
cpd-cli oadp backup create ${CPD_OPERATOR_BACKUP} --include-namespaces ibm-common-services --include-resources='namespaces,operatorgroups,configmaps,scheduling,crd' --skip-hooks --log-level=debug --verbose