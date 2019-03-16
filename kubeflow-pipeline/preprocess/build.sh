IMAGE=nvcrio.azurecr.io/sae/ananths:kubeflow-preprocess

docker build -t $IMAGE .
docker push $IMAGE
