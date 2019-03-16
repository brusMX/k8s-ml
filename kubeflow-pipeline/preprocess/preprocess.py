import os
import argparse
import numpy as np
import warnings
import wget
import zipfile
from helpers import process_image
from pathlib import Path
warnings.filterwarnings("error")



#pip install wget
def download_unzip_data(input_dir,url):
    filename = wget.download(url, input_dir)
    with zipfile.ZipFile(os.path.join(input_dir, filename),"r") as zip_ref:
        zip_ref.extractall(os.path.join(input_dir))


    
    


def save_data(processed_data, output_dir):
    (x_train, y_train), (x_test, y_test) = processed_data
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    np.save(os.path.join(output_dir, 'x_train.npy'), x_train)
    np.save(os.path.join(output_dir, 'y_train.npy'), y_train)
    np.save(os.path.join(output_dir, 'x_test.npy'), x_test)
    np.save(os.path.join(output_dir, 'y_test.npy'), y_test)
    np.save(   )






def get_dataset(base_path, file, image_size):
    warnings.filterwarnings('error')
    data = [str(f.absolute()) for f in Path(base_path).glob('**/*.jpg')]
    bad = []
    with open(file, "w") as f:
        for item in data:
            try:
                img, _ = process_image(item, 0, image_size)
                assert img.shape[2] == 3, "Invalid channel count"
                # write out good images
                f.write('{}\n'.format(item))
            except Exception as e:
                bad.append(item)
                print('{}\n{}\n'.format(e, item))
            except RuntimeWarning as w:
                bad.append(item)
                print('--------------------------{}\n{}\n'.format(w, item))

        print('{} bad images ({})'.format(len(bad), len(bad) / float(len(data))))
    return bad

if __name__ == "__main__":
    IMAGES="https://github.com/brusMX/k8s-ml/raw/kubeflow-pipelines/fotos.zip"
    parser = argparse.ArgumentParser(
    description='CNN Training for Image Recognition. Provide  input dir, output dir, data, dataset name and imagesize')
    parser.add_argument('--input_dir',
                        help='provide input directory')
    parser.add_argument('--output_dir',
                        help='provide output directory')
    parser.add_argument('-d', '--data', help='directory to training and test data', default='data')
    parser.add_argument('-t', '--target', help='target file to hold good data', default='dataset.txt')
    parser.add_argument('-i', '--img_size', help='target image size to verify', default=160, type=int)
    args = parser.parse_args()

    download_unzip_data(args.input_dir,IMAGES)
    get_dataset(args.data, args.target, args.img_size)
    
    print('input_dir: {}'.format(args.input_dir))
    print('output_dir: {}'.format(args.output_dir))



    # python clean.py -d data/PetImages -t dataset.txt

