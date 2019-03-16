# FROM nvcr.io/nvidia/tensorrtserver:19.02-py3
FROM nvcrio.azurecr.io/nvidia/tensorrtserver:alpha

RUN apt-get install -y software-properties-common && \
	add-apt-repository -y ppa:deadsnakes/ppa && \
	apt-get update && \
	apt-get install -y python3.6

COPY serve.py /scripts/serve.py
	
