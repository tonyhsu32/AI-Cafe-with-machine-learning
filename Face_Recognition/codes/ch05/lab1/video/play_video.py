import numpy as np
import cv2 as cv

cap = capture =cv.VideoCapture('chaplin.mp4')
while(cap.isOpened()):
    ret, frame = cap.read()

    if not ret:
        break

    cv.imshow('frame',frame)
    cv.waitKey(1)

cap.release()
cv.destroyAllWindows()