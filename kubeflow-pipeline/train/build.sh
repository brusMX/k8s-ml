IMAGE=nvcrio.azurecr.io/sae/ananths:kubeflow-train

docker build -t $IMAGE .
docker push $IMAGE
