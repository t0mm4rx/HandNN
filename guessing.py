from keras.models import load_model
from PIL import Image
import numpy as np
import subprocess

model = load_model('model.h5')

def take_snapshot():
    subprocess.call('fswebcam -d /dev/video1 -S 10 --no-banner -r 640x480 webcam.png', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

def get_image_data():
    im = Image.open('webcam.png').convert('L').resize((64, 64))
    return np.array(np.asarray(im) / 127.0 - 1.0).flatten()

def output_to_pred(output):
    if (output[0][0] > .1):
        return 'left'
    elif (output[0][1] > .1):
        return 'right'
    else:
        return 'no'

while True:
    take_snapshot()
    data = get_image_data()
    pred = output_to_pred(model.predict(np.array([data])))
    print(pred)
