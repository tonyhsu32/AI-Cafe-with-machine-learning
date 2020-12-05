from time import sleep
from picamera import PiCamera
import sys

if len(sys.argv) != 2:
    print('Usage:',sys.argv[0],'<filename>')
    sys.exit(2)

camera = PiCamera()
camera.resolution = (640, 480)
camera.start_preview()

# Camera warm-up time
sleep(1)

while True:
    k = input()
    break

camera.capture(sys.argv[1])

camera.stop_preview()
