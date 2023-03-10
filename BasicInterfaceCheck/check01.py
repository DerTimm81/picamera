# This script is simply check the connection to the Pi Camera of the Raspberry Pi module.
# Please be aware that this scrip will require you to run in "attached"-mode, 
# meaning that you have the Raspberry Pi module connected via HDMI to a monitor.

# loading the library for the Raspberry Pi Camera
from picamera import PiCamera

# loading some standard libraries from Python that we need to add time delays
from time import sleep

# Initializing the camera
camera = PiCamera()

# start full screen view of the live image
camera.start_preview()

# stay alive for 10 seconds
sleep(10)

# shutdown the full screen view and terminating the script
camera.stop_preview()
