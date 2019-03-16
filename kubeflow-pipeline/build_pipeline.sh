WORK_DIR=$(pwd)

# Build and push images of kubeflow pipeline components
cd $WORK_DIR/preprocess && ./build.sh && \
cd $WORK_DIR/train && ./build.sh && \
cd $WORK_DIR/serve && ./build.sh && \

# Compile kubeflow pipeline tar file 
cd $WORK_DIR/pipeline && ./build.sh


