import cv2
import time

def convertToRGB(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#load test iamge
test1 = cv2.imread('car_number.jpg')

#convert the test image to gray image as opencv face detector expects gray images 
gray_img = cv2.cvtColor(test1, cv2.COLOR_BGR2GRAY)

#load cascade classifier training file for haarcascade
haar_face_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_russian_plate_number.xml')

#let's detect multiscale (some images may be closer to camera than others) images 
cars = haar_face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5);  

#print the number of car plates found
print('Car plate found: ', len(cars))

#go over list of car plates and draw them as rectangles on original colored
for (x, y, w, h) in cars:
    cv2.rectangle(test1, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('Test Imag', test1) 
cv2.waitKey(0) 
cv2.destroyAllWindows()


