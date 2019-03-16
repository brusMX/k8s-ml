CLIENT_DIR=$(pwd)/trtis_client
REPO_DIR=/tmp/tensorrt-inference-server
SCRIPT_DIR=$REPO_DIR/src/clients/python/
IMAGE=tensorrtserver_clients
UPDATED_CLIENT_FILE=updated_image_client.py
DEMO_CLIENT_UI=demo_client_ui.py

CMD="pip install dash && python3 /workspace/src/clients/python/$DEMO_CLIENT_UI"
# If you don't want to test the UI, just use the command below
# CMD="python3 /workspace/src/clients/python/$UPDATED_CLIENT_FILE -m resnet_graphdef -s RESNET images/mug.jpg"

git clone https://github.com/NVIDIA/tensorrt-inference-server.git $REPO_DIR 
cp $CLIENT_DIR/$UPDATED_CLIENT_FILE $SCRIPT_DIR
cp $CLIENT_DIR/$DEMO_CLIENT_UI $SCRIPT_DIR
docker build -t $IMAGE -f $REPO_DIR/Dockerfile.client $REPO_DIR
docker run -it --rm --net=host $IMAGE /bin/bash -c "$CMD"
