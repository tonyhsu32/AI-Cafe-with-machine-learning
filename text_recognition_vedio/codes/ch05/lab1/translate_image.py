import numpy as np
import cv2 as cv

# Load an color image in grayscale
img = cv.imread('mybaby.jpg',cv.IMREAD_GRAYSCALE)

rows,cols = img.shape
M = np.float32([[1,0,100],[0,1,50]])
dst = cv.warpAffine(img,M,(cols,rows))

cv.imshow('translation image',dst)
cv.waitKey(0)
cv.destroyAllWindows()
