import numpy as np
import cv2 as cv

# Load an color image in grayscale
img = cv.imread('mybaby.jpg',0)

# zoom image
height, width = img.shape[:2]
res = cv.resize(img,(2*width, 2*height), interpolation = cv.INTER_CUBIC)
cv.imshow('zoom image',res)

# shrink image, using other parameters
res = cv.resize(img,None,fx=0.5, fy=0.5, interpolation = cv.INTER_AREA)
cv.imshow('shrink image',res)

cv.waitKey(0)
cv.destroyAllWindows()

#cv.imwrite('otherbaby.jpg',res)

