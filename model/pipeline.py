import json
import sys
import os
from pathlib import Path
def get_data():
    path = Path(os.path.abspath(__file__)).parent.parent
    path = os.path.join(path, 'dataset')
    path = os.path.join(path, 'transcriptions.json')

    with open(path, 'r') as f:
        data = json.load(f)

    data_imp = {}
    for obj in data:
        img = obj['img']
        text = obj['text']
        data_imp[img] = text

    return data_imp

def load_image(image_path):
    path = Path(os.path.abspath(__file__)).parent.parent
    path = os.path.join(path, 'dataset')
    path = os.path.join(path, 'img')
    path = os.path.join(path, image_path)
    return path

if __name__ == '__main__':
    ds = get_data()
    for i in ds.keys():
        print(load_image(i))
