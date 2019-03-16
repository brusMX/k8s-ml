# Modify according to your persistent-volume.yaml
PERSISTENT_VOL_PATH=/mnt/workspace

sudo mkdir $PERSISTENT_VOL_PATH

kubectl create -f pipeline/persistent-volume.yaml
kubectl create -f pipeline/persistent-volume-claim.yaml

