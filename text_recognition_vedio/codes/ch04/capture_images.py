from time import sleep
from picamera import PiCamera
import sys
import os

if len(sys.argv) != 4:
    print("Usage:",sys.argv[0],"<foldername> <start#> <# of images>")
    exit(2)

if not os.path.exists(sys.argv[1]):
    os.makedirs(sys.argv[1])

camera = PiCamera()
camera.resolution = (640, 480)
camera.start_preview()

# Camera warm-up time
sleep(1)

nstart=int(sys.argv[2])
nstop=nstart+int(sys.argv[3])

for i in range(nstart,nstop):
    while True:
        k = input()
        break

    pname=sys.argv[1]+'/'+str(i)+'.jpg'
    camera.capture(pname)
    print(pname,'saved...')

camera.stop_preview()
