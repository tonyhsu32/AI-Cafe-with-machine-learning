import numpy as np
import cv2
import sys

if len(sys.argv) != 2:
    print('Usage:',sys.argv[0],'<video name>')
    sys.exit(2)

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(sys.argv[1],fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    
    if ret==True:
        # write the frame
        out.write(frame)
        cv2.imshow('frame',frame)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()

