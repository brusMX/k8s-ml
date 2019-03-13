import json
import time
import datetime
import numpy as np
import tensorflow as tf
from io import StringIO

from azureml.core.model import Model

def init():
    global model

    try:
        model_path = Model.get_model_path('modelname')
    except:
        model_path = 'model.pb'

    with tf.gfile.GFile(model_path, "rb") as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())

    with tf.Graph().as_default() as graph:
        tf.import_graph_def(graph_def, name='model')

    print('Initialized model "{}" at {}'.format(model_path, datetime.datetime.now()))
    model = graph


def load_graph(model_file):
    graph = tf.Graph()
    graph_def = tf.GraphDef()

    with open(model_file, "rb") as f:
        graph_def.ParseFromString(f.read())
    with graph.as_default():
        tf.import_graph_def(graph_def)

    return graph

def run(raw_data):
    global model
    prev_time = time.time()
          
    post = json.loads(raw_data)
    

    current_time = time.time()
    inference_time = datetime.timedelta(seconds=current_time - prev_time)

    payload = {
        'time': inference_time.total_seconds(),
        'prediction': 3,
        'scores': [1,2,2]
    }

    print('Input ({}), Prediction ({})'.format(post['image'], payload))

    return payload

if __name__ == "__main__":
    g = load_graph('model.pb')
    #init()
    #out = run({x="@"})