import numpy as np
import cv2 as cv

# Load an color image in grayscale
img = cv.imread('mybaby.jpg',0)

cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
