from picamera import PiCamera

vlen=20
camera = PiCamera()
camera.resolution = (320, 240)

camera.start_preview()

camera.start_recording('video.h264')
camera.wait_recording(vlen)
camera.stop_recording()

camera.stop_preview()
