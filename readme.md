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

### SubSubSub Title