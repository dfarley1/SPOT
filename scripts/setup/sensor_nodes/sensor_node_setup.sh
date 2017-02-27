# This file sets up Sensor nodes

# This allows us to bypass any password intensive commands espcially for file transfers
sudo apt-get install sshpass

# This allows us to use the GPIO pins on the Raspberry Pi
sudo apt-get install python-dev python-rpi.gpio

# Any installation script for CV side of setup
#sudo ./david's script for setting up the CV

# This generates a cookies file upon setup.
sudo pip install runp
runp /home/pi/SPOT/Cloud/testHttp.py testGET

# This sets up the sensor for autonomous background script
sudo cp /home/pi/SPOT/scripts/setup/sensor_nodes/bootup_ping_script.sh /etc/init.d/
sudo update-rc.d bootup_ping_script.sh defaults

echo "Sensor setup complete!"

sudo reboot

