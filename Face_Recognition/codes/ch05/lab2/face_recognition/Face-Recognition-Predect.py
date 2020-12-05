
# coding: utf-8

# Face Recognition with OpenCV

# To detect faces, I will use the code from my previous article on [face detection](https://www.superdatascience.com/opencv-face-detection/). So if you have not read it, I encourage you to do so to understand how face detection works and its Python coding. 

# ### Import Required Modules

# Before starting the actual coding we need to import the required modules for coding. So let's import them first. 
#
# - **cv2:** is _OpenCV_ module for Python which we will use for face detection and face recognition.
# - **os:** We will use this Python module to read our training directories and file names.
# - **numpy:** We will use this module to convert Python lists to numpy arrays as OpenCV face recognizers accept numpy arrays.

# In[1]:

#import OpenCV module
import cv2
#import os module for reading training data directories and paths
import os
#import numpy to convert python lists to numpy arrays as
#it is needed by OpenCV face recognizers
import numpy as np
import sys
from utilities import detect_face

if len(sys.argv) != 2:
    print('Usage:',sys.argv[0],'<lable file>')
    sys.exit(2)

#there is no label 0 in our training data so subject name for index/label 0 is empty
#read label
#subjects = ["", "Ramiz Raja", "Elvis Presley", "Tim Yang"]
subjects=['']
with open(sys.argv[1]) as fp:
    for data in fp:
        subjects+=[data.strip('\n')]

#create our LBPH face recognizer
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

#read trained data
face_recognizer.read('training-data/trainner.yml')
        
# ### Prediction

# Now comes my favorite part, the prediction part. This is where we actually get to see if our algorithm is actually recognizing our trained subjects's faces or not. We will take two test images of our celeberities, detect faces from each of them and then pass those faces to our trained face recognizer to see if it recognizes them.
#
# Below are some utility functions that we will use for drawing bounding box (rectangle) around face and putting celeberity name near the face bounding box.

# In[8]:

#function to draw rectangle on image
#according to given (x, y) coordinates and
#given width and heigh
def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

#function to draw text on give image starting from
#passed (x, y) coordinates.
def draw_text(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)


# First function `draw_rectangle` draws a rectangle on image based on passed rectangle coordinates. It uses OpenCV's built in function `cv2.rectangle(img, topLeftPoint, bottomRightPoint, rgbColor, lineWidth)` to draw rectangle. We will use it to draw a rectangle around the face detected in test image.
#
# Second function `draw_text` uses OpenCV's built in function `cv2.putText(img, text, startPoint, font, fontSize, rgbColor, lineWidth)` to draw text on image.
#
# Now that we have the drawing functions, we just need to call the face recognizer's `predict(face)` method to test our face recognizer on test images. Following function does the prediction for us.

# In[9]:

#this function recognizes the person in image passed
#and draws a rectangle around detected face with name of the
#subject
def predict(test_img):
    #make a copy of the image as we don't want to chang original image
    img = test_img.copy()
    #detect face from the image
    face, rect = detect_face(img)

    if face is None or rect is None:
        return test_img

    #predict the image using our face recognizer
    label, confidence = face_recognizer.predict(face)
    
    print('confidence:',confidence)
     
    #get name of respective label returned by face recognizer
    #label_text = subjects[label]
    label_text = subjects[label] if confidence <50 else subjects[0]

    #draw a rectangle around face detected
    draw_rectangle(img, rect)
    #draw name of predicted person
    draw_text(img, label_text, rect[0], rect[1]-5)

    return img

# Now that we have the prediction function well defined, next step is to actually call this function on our test images and display those test images to see if our face recognizer correctly recognized them. So let's do it. This is what we have been waiting for.

# In[10]:

print("Predicting images...")

test_images_names = os.listdir("test-data")

#go through each test image name, read image,
#predict face
for image_name in test_images_names:
    #ignore system files like .DS_Store
    if image_name.startswith("."):
        continue;

    #load test images
    test_img = cv2.imread("test-data/"+image_name)

    #perform a prediction
    predicted_img = predict(test_img)

    #display image
    cv2.imshow('Predicted', cv2.resize(predicted_img, (400, 500)))
    cv2.waitKey(0)

print("Prediction complete")

cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.destroyAllWindows()
