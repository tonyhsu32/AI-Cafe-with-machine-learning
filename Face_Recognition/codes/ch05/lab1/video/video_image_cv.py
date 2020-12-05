import numpy as np
import cv2 as cv
import sys

if len(sys.argv) != 2:
    print('Usage:',sys.argv[0],'<image name>')
    sys.exit(2)

# Capture video cam
cap = cv.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv.imshow('frame',frame)

    key = cv.waitKey(1)
    if key & 0xFF == ord('q'):
        break

    if key & 0xFF == ord('p'):
        cv.imwrite(sys.argv[1],frame)
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
