# This file set up Sensor Nodes
#-------------------------------
# This allows us to bypass any password intensive commands especially for file transfers
sudo apt-get install sshpass
#------------------------------
# This allows us to use the GPIO pins on the Raspberry Pi
sudo apt-get install python-dev python-rpi.gpio
#------------------------------
#set up for neopixel ring library with python wrapper
cd ~/
sudo apt-get update
sudo apt-get install build-essential python dev git scons swig
cd ~
git clone https://github.com/jgarff/rpi_ws281x.git
cd ~/rpi_ws281.x
scons
sudo python /home/pi/rpi_ws281.x/setup.py install
#------------------------------ 
# any installation script for CV side of setup
# sudo ./david's script for setting up the CV
#------------------------------
# This generates a cookies file upon setup
sudo pip install runp
sudo runp /home/pi/SPOT/Cloud/testHttp.py sensor_getUUID_GET
sudo runp /home/pi/SPOT/Cloud/testHttp.py sensor_GET
#------------------------------
sudo mkdir ~/spot_log
sudo chown pi:pi ~/spot_log
sudo echo '0' >~/spot_log/license_log.txt
sudo echo '' >~/spot_log/occupied_since.txt
sudo echo '' >~/spot_log/uuid_file.txt
#------------------------------
# This sets up the sensor for autonomous background script
sudo cp /home/pi/SPOT/scripts/setup/sensor_nodes/bootup_ping_script.sh /etc/init.d/
sudo update-rc.d /etc/init.d/bootup_ping_script.sh defaults
#------------------------------
#------------------------------
echo "Sensor setup complete!"
#------------------------------
#------------------------------
sudo reboot
