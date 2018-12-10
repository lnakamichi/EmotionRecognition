import os
import glob
import path
import cognitive_face as CF


# Generate list of image files
img_dir = "./Test_Images/" # Path to directory containing test images
data_path = os.path.join(img_dir,'*g')
files = glob.glob(data_path)

# Subscription Key
KEY = '9f95ee5b824b4688a1eabe1e5b15225d'
CF.Key.set(KEY)

# API Endpoint
BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'
CF.BaseUrl.set(BASE_URL)

# Image URL
IMAGE_URL = 'file://localhost/Users/laurennakamichi/CSC480/EmotionRecognition/'

for f in files:
    print(IMAGE_URL + f)
    result = CF.face.detect(IMAGE_URL)
    print(result)
