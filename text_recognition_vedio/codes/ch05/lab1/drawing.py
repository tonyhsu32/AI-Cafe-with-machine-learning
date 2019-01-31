import numpy as np
import cv2 as cv

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv.line(img,(0,0),(511,511),(255,0,0),5)

# Draw rectangle
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)

# Draw circle
cv.circle(img,(447,63), 63, (0,0,255), -1)

# Draw Ellipse
cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

# Draw polygon
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((4,1,2))
cv.polylines(img,[pts],True,(0,255,255))


#Put Text
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'Raspberry Pi',(0,300),font,4,255,6,cv.LINE_AA)


# Show image
cv.imshow('Drawing',img)
cv.waitKey(0)
cv.destroyAllWindows()
