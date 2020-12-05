import numpy as np
import cv2 as cv
import imutils 

# Load an color image in grayscale
img = cv.imread('mybaby.jpg',cv.IMREAD_GRAYSCALE)

rows,cols = img.shape

# cols-1 and rows-1 are the coordinate limits
M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
dst = cv.warpAffine(img,M,(cols,rows))

#opencv turtoial2018
rotated = imutils.rotate_bound(dst, -45)
cv.imshow("Imutils Bound Rotation", rotated)
cv.waitKey(0)
cv.destroyAllWindows()



