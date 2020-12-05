import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2 as cv
import sys

if len(sys.argv) != 2:
    print('Usage:',sys.argv[0],'<image name>')
    sys.exit(2)

# Capture pi camera
camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # Capture frame-by-frame
    image = frame.array
    
    # Display the resulting frame
    cv.imshow('frame',image)
    
    key = cv.waitKey(1)
    if key & 0xFF == ord('q'):
        break

    if key & 0xFF == ord('p'):
        cv.imwrite(sys.argv[1],image)
        break
        
    rawCapture.truncate(0)

# When everything done, release the capture
cv.destroyAllWindows()
