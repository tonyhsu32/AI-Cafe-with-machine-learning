# using cv2 module
import numpy as np
import argparse
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
    help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)

# Otsu threshold
th2,img2 = cv2.threshold(image,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
print("Otsu’s threshold: {}".format(th2))
cv2.imshow("Otsu", img2)

# Otsu's thresholding after Gaussian filtering
th3,img3 = cv2.threshold(blurred,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
print("Otsu’s threshold after Gaussian blur: {}".format(th3))
cv2.imshow("Otsu blur", img3)

cv2.waitKey(0)
