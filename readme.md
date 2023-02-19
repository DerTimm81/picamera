# Introduction
In the year 2020, in the middle of the COVID pandemic, I started to play around with the Raspberry Pi 4 and coded quite a bit in Python 3 at that time. However, I kind of lost traction in that due to my busy work and re-engaged in that field in 2023. Trying to keep track of what I did three years ago, I failed to find and understand the code and had to start from scratch. That's why I promised myself to do better and document all I do. And here is, what we are going to do:

## What we will implement
I very much like image processing based projects. That's why we will use the Raspberry Pi 4 cameara module to perceive the environment and detect certain things. I will walk the user through every step, basically starting from a plain "I've bought stuff online"-situation and set everything up with the user.

TODO: Describe the project in more detail.

### Hardware List
Here comes the hardware used in this project:
* Raspberry Pi 4 B module
* SD Card (64Gbyte)
* USB-C Power Supply for the Raspberry Pi 4
* Keyboard and Mouse of the Rasberry Pi 4
* Raspberry Pi 4 Camera Module
* Parallel Serial Interface Cable between the Camera Module and the Raspberry Pi 4

### Software Configuration
We will use the basic Raspberry Pi 4 standard installation (please find details below). During the installation, we will make use of various Python Libraries that help us to achieve our goals. Please find the comprehensive list below. The version of Python 3 being used and library versions may vary depending on the date of your implementation. Please let me know if you encounter issues, so we can resolve it together.

### Software List
* Python vx.y.z
* Python Libraries:
    * Library A
    * Library B

# Getting Started
## Setting Up the Raspberry Pi 4 on a Mac

First of all, we need to give our Raspberry Pi 4 a basic image. We do that by downloading the IMAGER from the raspberry pi website:
https://www.raspberrypi.com/software/

We use the RASPBERRY PI OS (32-Bit) image and load that on the micro SD card. Writing the image to the SD card might take a while. After that is done, we eject the micro SD from the Mac and put in our Raspberry Pi module. Once done, we plug in the USB-C power cable to the Raspberry Pi 4. We also connect the HDMI cable to a monitor, so we can monitor the boot sequence on the screen.

We follow the boot sequence and create a user (username: timm, password: timm) and connect it to the local wifi network.

## Preparing the Visual Studio Code on the Mac that we will use to code

On our Mac machine, we load and start Visual Studio Code. Once started, we will install the "SSH" plugin by looking for the extention inside Visual Studio Code which says "SSH" and comes from Microsoft.

Once installed, we hit COMMAND + SHIFT + P to establish a connection to the Raspberry Pi. The Raspberry Pi should show up as "rasberrypi.local" in the popup-menu. If that fails, we might need to delete previous configurations on our Mac by starting the Terminal and typing:

<pre>
<code>
ssh-keygen -R 192.168.XXX.YYY
</code>
</pre>

Of course, you might need to replace the XXX and YYY with the IP address of your Raspberry Pi. You might be asked by your Mac to confirm the removal of previous configurations by entering your Mac password as this is a quite deep-level change.

### Making It Easier to Connect to the Raspberry Pi via SSH in your network

I got quite annoyed re-entering my credentials to my remote connection over and over again. That's why I followed the instructions in this Youtube tutorial to have an easy SSH connection to my raspberry Pi:

https://www.youtube.com/watch?v=w6OsICbnJbA

### Connecting the Raspberry Pi to Github for easier source code version control

One of my learnings from the past was, that I do not want code to exist only locally. That's why I wanted this code to be controlled via GitHub. That caused the need to generate an SSH Key for the Raspberry Pi that would be known by GitHub. I followed the instructions of the linked page to generate an SSH Key on the Raspberry Pi and familiarize that to GitHub.

https://docs.github.com/de/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

In doing that, I ensured, that when I work remotely on the Raspberry Pi Module via my Visual Studio Code installation on my Mac, I would still be able to push source code changes to GitHub directly. I also learnt, that having a connection between my Mac and GitHub will not be enough, as when working remotely, you will need to generate an SSH key on the Raspberry Pi directly to be able to push source code changed to GitHub directly.

## Getting the Source Code onto your Raspberry Pi

With the remote connection established inside Visual Studio Code and being on the device now, I checked out the repository of this project onto the Raspberry Pi via Visual Studio Code. Simply use the SSH-definitions of this repository and check out the code.

## Before working with the camera

The image you just loaded to the Raspberry Pi 4 via the above installation instructions might not be the latest and greatest. That's why you will start the Terminal in Visual Studio Code. That Terminal should indicate to you that you are running on the Raspberry Pi showing somthing like. "timm@raspberrypi.local". If that is the case, we will run the below two commands to update all modules that exist on the Raspberry Pi now:

<pre>
<code>
sudo apt-get upgrade
</code>
</pre>

... will compare the installed packages to the available ones. 

<pre>
<code>
sudo apt-get update
</code>
</pre>

... will then install updates - if any - to the Raspberry Pi. Please note that you might need to hit "Y" or "Yes" to confirm that updates are going to be installed on the Raspberry Pi. All of that might take a while. Please be patient.

After that, please enter:

<pre>
<code>
sudo reboot
</code>
</pre>

... That will re-start the Raspberry Pi with all new modules. Please still ensure, that you have your Raspberry Pi connected to the monitor via HDMI. We will still need that user interface to further configure some stuff. Visual Studio Code will, in the lower left corner, indicate that it is re-connecting to the Raspberry Pi. Please confirm any "Refresh"-message to ensure, you are re-connected to the Raspberry Pi after rebooting.

After the reboot is finished, please run the below command via the Terminal 

<pre>
<code>
sudo apt-get install python-picamera python3-picamera
</code>
</pre>

... This will install python packages needed to properly access the Raspberry Pi camera module you are about to interface. "python-picamera" ia Python 2 module that might not be supported anymore at the time you run the command. You might get an error message. If that is the case, simplify the above command to:

<pre>
<code>
sudo apt-get install python3-picamera
</code>
</pre>

... That will install the Raspberry Pi Camera Support for Python 3 only. That will be enough, as we will use Python 3 anyways going forward. Please carefully read the console output. You might see a mesage like: "already installed". If that is the case, everything is fine, as the above general update-command for all packages might have installed that package already.

### Setting up the Keyboard

Have you tried to type "y" on the keyboard connected to the Raspberry Pi, but "z" was typed? If that is the case, please go to "Settings" on the Raspberry Pi via the graphical user interface on the HDMI-connected screen and hange the "Mouse and Keybard Setttings" under "Keyboard" to the layout and variant you are using. In my case, this is "German", but it might differ for you. If you are based out of an English country (US, GB, ...), and you type "y" and it really types "y" on the screen, everything is fine and you don't need to adjust anything.

### Enabling the Camera I/O

As a default, the camera interface on the Raspberry Pi is deactivated. Before we can truly interface the images, you need to run the Terminal on the Raspberry Pi. I anticipate, that you have the Raspberry Pi still connected to a keyboard and an HDMI-based monitor, so that you are able to run the Terminal easily on the Raspberry Pi. Please do so, if that is not the case.

Now run:

<pre>
<code>
sudo raspi-config
</code>
</pre>

What is going to show up id a fairly outdated graphical user interface from the 90ies with an entry called "Interfaces", from which you select "I1" to enable "Cameara Support". That step is crucial for the below steps, as otherwise, the scripts will fail to run.


# Checking the Connection to the PiCamera Module

Once you checked out the project (THIS ONE!) from GitHub, you should now see a folder called "BasicInterfaceCheck". Inside that folder, you should have a file called "check01.py". That file will only work nicely if you still have the Raspberry Pi connected via HDMI to a monitor and the image from the previous step is fully loaded.

If that is indeed the case, you can open "Thonny" from the Raspberry Pi installation using the user interace. Inside "Thonny" you should now be able to open the "check01.py" file and hit the "Play" button. What should happen is once you run the script, the camera image should show in full screen fro 10 seconds until it terminates. Please ensure, this is the case.

If you encounter an error, you might need to install the picamera package to python so you are able to access the camera.