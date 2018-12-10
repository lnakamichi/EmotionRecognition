import sys, os
import cv2
import glob
import keras
import numpy as np
import pandas as pd
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from keras.models import Sequential
from keras.models import load_model
from keras.losses import categorical_crossentropy
from keras.optimizers import Adam
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator

img_dir = "./Test_Images/" # Path to directory containing test images
data_path = os.path.join(img_dir,'*g')
files = glob.glob(data_path)
model = load_model("./model.h5") # Path to directory containing model
model.compile(optimizer = 'adam', loss = 'categorical_crossentropy',
              metrics = ['accuracy'])

# captures video from camera
cap = cv2.VideoCapture(0)
# face cascade to identify face in image
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

def display_graph(emotions):
   objects = ('Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral')
   y_pos = np.arange(len(objects))
   plt.figure("Classification Percentage")
   thismanager = plt.get_current_fig_manager()
   # Change size of window for figure 1
   thismanager.window.wm_geometry("+0+0")
   # thismanager.window.wm_geometry("200+0")
   plt.bar(y_pos, emotions, align='center',alpha=1)
   plt.xticks(y_pos, objects)
   plt.ylabel('Percentage')
   plt.title('Emotions')

#for f1 in files:
while 1:
   # Path to haarcascade file
   #img = cv2.imread(f1)
   ret, img = cap.read()

   gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   faces = face_cascade.detectMultiScale(gray, 1.3, 5)
   for (x, y, w, h) in faces:
      crop_img = gray[y:y+h, x:x+w]
      resized = cv2.resize(crop_img, (48, 48), interpolation = cv2.INTER_AREA)
      arr = image.img_to_array(resized)
      arr = np.expand_dims(arr, axis = 0)
      arr /= 255
      predictions = model.predict(arr)
      display_graph(predictions[0])
      plt.figure("Facial Expression")
      thismanager = plt.get_current_fig_manager()
      # Change size of window for figure 2
      thismanager.window.wm_geometry("+850+0")

      cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
      plt.imshow(img)
      plt.show(block=False)
      plt.pause(3)
      plt.close('all')

