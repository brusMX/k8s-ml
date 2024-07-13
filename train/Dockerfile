FROM tensorflow/tensorflow:1.13.1

WORKDIR /

COPY ./images /images
COPY ./retrain.py /retrain.py

ENTRYPOINT [ "python","retrain.py" ]