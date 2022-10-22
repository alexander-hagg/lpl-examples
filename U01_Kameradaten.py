from time import sleep
from picamera import PiCamera


camera = PiCamera()
# camera.start_preview()
for filename in camera.capture_continuous('img{timestamp:%Y-%m-%d-%H-%M}.jpg'):
    sleep(1)
    print('Captured %s' % filename)
