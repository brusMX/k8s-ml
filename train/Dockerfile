FROM tensorflow/tensorflow:1.15.4

WORKDIR /

COPY ./images /images
COPY ./retrain.py /retrain.py

ENTRYPOINT [ "python","retrain.py" ]