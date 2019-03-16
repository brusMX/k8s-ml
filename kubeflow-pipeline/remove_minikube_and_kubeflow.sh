# Remove KubeFlow
cd ${KUBEFLOW_SRC}/${KFAPP}
${KUBEFLOW_SRC}/scripts/kfctl.sh delete k8s

# Remove Minikube
minikube stop
minikube delete
