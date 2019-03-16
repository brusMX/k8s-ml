IMAGE=nvcrio.azurecr.io/sae/ananths:kubeflow-serve

docker build -t $IMAGE .
docker push $IMAGE
