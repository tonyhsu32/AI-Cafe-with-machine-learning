import numpy as np
import imutils
from imutils.video import VideoStream
from imutils.video import FPS
import cv2 as cv
import sys
import time

if len(sys.argv) != 2:
    print('Usage:',sys.argv[0],'<image name>')
    sys.exit(2)

# initialize the video stream, allow the cammera sensor to warmup,
# and initialize the FPS counter
print("[INFO] starting video stream...")
#vs = VideoStream(src=0).start()
vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)
fps = FPS().start()
    
while True:
    # grab the frame from the threaded video stream
    frame = vs.read()

    # Display the resulting frame
    cv.imshow('frame',frame)
    
    key = cv.waitKey(1)
    if key & 0xFF == ord('q'):
        break

    if key & 0xFF == ord('p'):
        cv.imwrite(sys.argv[1],frame)
        break

# When everything done, release the capture
cv.destroyAllWindows()
