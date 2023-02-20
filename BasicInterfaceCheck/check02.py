# This script simply captures a picture from the camera and 
# is saving it unter the outputs-folder in the BasicInterfaceChecks.
# This script works fully remotely and does not require 
# an HDMI-cable connected to the Raspberry Pi.

from picamera import PiCamera
import os

camera = PiCamera()
cwd = os.getcwd()
pathToWrite = cwd + "/BasicInterfaceCheck/outputs/check02.jpg"

camera.capture(pathToWrite)