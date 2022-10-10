# cpd-cli oadp client config set namespace=oadp-operator
# cpd-cli oadp client config set cpd-namespace=cpd-instance
# cpd-cli oadp backup create --include-namespaces=cpd-instance --exclude-resources='Event,Event.events.k8s.io' --default-volumes-to-restic --snapshot-volumes=false --cleanup-completed-resources cpd-instance-backup --log-level=debug --verbose
chmod 700 cpd-operators.sh
./cpd-operators.sh backup --foundation-namespace ibm-common-services --operators-namespace ibm-common-services
oc get configmap cpd-operators -n ibm-common-services
cpd-cli oadp backup create cpdbr-operators --include-namespaces ibm-common-services --include-resources='namespaces,operatorgroups,configmaps,scheduling,crd' --skip-hooks --log-level=debug --verbose