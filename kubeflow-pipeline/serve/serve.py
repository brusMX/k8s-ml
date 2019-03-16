import os
import shutil
import argparse


parser = argparse.ArgumentParser(
    description='Provide input directory')
parser.add_argument('--input_dir',
                    help='provide input directory')
args = parser.parse_args()


TRTIS_RESOURCE_DIR = "trtis_resource"

# Modify according to your training script and config.pbtxt
GRAPHDEF_FILE = "trt_graphdef.pb"
MODEL_NAME = "resnet_graphdef"

# Check for resource dir
resource_dir = os.path.join(args.input_dir, TRTIS_RESOURCE_DIR)
if not os.path.isdir(resource_dir):
    raise IOError("Resource dir for TRTIS not found")

# Create a directory structure that TRTIS expects
config_file_path = os.path.join(resource_dir, "config.pbtxt")
label_file_path = os.path.join(resource_dir, "labels.txt")
graphdef_path = os.path.join(args.input_dir, GRAPHDEF_FILE)
model_dir = '/models/%s/1' % MODEL_NAME

os.makedirs(model_dir)
shutil.copy(config_file_path, '/models/%s' % MODEL_NAME)
shutil.copy(label_file_path, '/models/%s' % MODEL_NAME)
shutil.copyfile(graphdef_path, os.path.join(model_dir, 'model.graphdef'))

os.system("trtserver --model-store=/models")
