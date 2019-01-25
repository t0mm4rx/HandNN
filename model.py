from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import glob

from keras.models import Sequential
from keras.layers import Dense, Activation

"""
    Getting data
"""

def get_image_data(path):
    im = Image.open(path).convert('L').resize((64, 64))
    return np.array(np.asarray(im) / 127.0 - 1.0).flatten()

def get_dataset():
    features = []
    targets = []
    for file in glob.glob("data/left2/*.png"):
        features.append(get_image_data(file))
        targets.append([1.0, 0.0])
    for file in glob.glob("data/right2/*.png"):
        features.append(get_image_data(file))
        targets.append([0.0, 1.0])
    return (np.array(features), np.array(targets))


"""
    Training
"""

print('Loading training data...')
(features, targets) = get_dataset()

model = Sequential()
model.add(Dense(100, input_dim=4096))
model.add(Activation('sigmoid'))
model.add(Dense(2, input_dim=100))
model.add(Activation('sigmoid'))

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
model.fit(features, targets, batch_size=64, epochs=1000)
model.save('model.h5')
