import numpy as np
import cv2 as cv

image = cv.imread('mybaby.jpg')
cv.imshow("Original", image)

cropped = image[0:190, 125:300]
cv.imshow("Baby Face", cropped)
cv.waitKey(0)
