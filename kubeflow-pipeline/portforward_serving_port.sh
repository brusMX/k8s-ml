# Look for the name of the serving POD mentioned on the Kubeflow pipeline dashboard
SERVING_POD=resnet-cifar10-pipeline-8tkrt-1130129541

HOST_PORT=8000

# Model name specified in the file cofig.pbtxt
MODEL_NAME=resnet_graphdef

apt-get update && apt-get install -y socat
kubectl port-forward pod/$SERVING_POD $HOST_PORT:8000 -n kubeflow &
curl localhost:$HOST_PORT/api/status/$MODEL_NAME
