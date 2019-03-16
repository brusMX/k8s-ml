#FROM nvcr.io/nvidia/tensorflow:19.02-py3
FROM tensorflow/tensorflow:1.9.0


RUN pip install wget pathlib

COPY preprocess.py /scripts/preprocess.py
COPY helpers.py /scripts/helpers.py
RUN mkdir /scripts/data

ENTRYPOINT [ "python","/scripts/preprocess.py"]