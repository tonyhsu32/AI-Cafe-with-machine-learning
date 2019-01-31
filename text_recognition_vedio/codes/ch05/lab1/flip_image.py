import numpy as np
import cv2 as cv

image = cv.imread('mybaby.jpg')
cv.imshow("Original", image)

flipped = cv.flip(image, -1)
cv.imshow("Flipped Horizontally", flipped)

cv.waitKey(0)
cv.destroyAllWindows()