import cv2
import time

def convertToRGB(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#load test iamge
test1 = cv2.imread('/home/ubuntu/Desktop/codes/ch04/s3/test.jpg')

#convert the test image to gray image as opencv face detector expects gray images 
gray_img = cv2.cvtColor(test1, cv2.COLOR_BGR2GRAY)

#load cascade classifier training file for haarcascade
haar_face_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml')

#let's detect multiscale (some images may be closer to camera than others) images 
faces = haar_face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5);  

#print the number of faces found
print('Faces found: ', len(faces))
