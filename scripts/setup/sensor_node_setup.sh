#!/bin/bash
# This file sets up Sensor nodes

# This allows us to bypass any password intensive commands espcially for file transfers
sudo apt-get install sshpass

# This allows us to use the GPIO pins on the Raspberry Pi
sudo apt-get install python-dev python-rpi.gpio

# Any installation script for CV side of setup
#sudo ./david's script for setting up the CV