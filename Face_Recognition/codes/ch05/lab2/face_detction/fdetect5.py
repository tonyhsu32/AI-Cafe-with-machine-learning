#!/usr/bin/python3

import cv2
import time
from picamera import PiCamera

img_name='/home/pi/image.jpg'
img_out='/home/pi/result.jpg'

def convertToRGB(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

camera = PiCamera()
time.sleep(1)
camera.capture(img_name)

#load test iamge
test1 = cv2.imread(img_name)

#convert the test image to gray image as opencv face detector expects gray images 
gray_img = cv2.cvtColor(test1, cv2.COLOR_BGR2GRAY)

#load cascade classifier training file for haarcascade
haar_face_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml')
#haar_face_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_eye.xml')
#haar_face_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/lbpcascades/lbpcascade_frontalface_improved.xml')

#let's detect multiscale (some images may be closer to camera than others) images 
faces = haar_face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5);  

#print the number of faces found
print('Faces found: ', len(faces))

#go over list of faces and draw them as rectangles on original colored
for (x, y, w, h) in faces:
    cv2.rectangle(test1, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imwrite(img_out, test1) 

