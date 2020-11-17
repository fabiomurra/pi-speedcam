# day 1:
# trying to get the camera to work
# instructions here:  https://www.youtube.com/watch?v=FPaNpiLVAfM

# day 2:
# setting up the dev environment
# VSCode remote dev on the raspberry pi

# day 3:
# setting up git
# added git with VS Code server
# now trying to link it to my github repo

# import
from picamera import PiCamera
from time import sleep

#setup
camera = PiCamera()
camera.start_preview()

# wait for the sensor to set its brightness 
# it takes at least 2 seconds
sleep(3)

# capture a picture
camera.capture('/home/pi/cam/pics/image2.jpg')

# stop the camera
camera.stop_preview()
