This is a README for the ping sensor setup.

For new raspberry pi units, the hardware must be updated. 

1. sudo python

-- import RPi.GPIO as GPIO

-- GPIO.VERSION

-- exit

2. If device version less than 0.54, update:

-- sudo apt-get install update
 
-- sudo apt-get install upgrade

Reference: http://makezine.com/projects/tutorial-raspberry-pi-gpio-pins-and-python/


GPIO Pins 23 and 24 are designated for operating the HC-SR04 ultrasonic ping sensor. Trigger will be used to enable the ping sensor for measuring distances, whereas echo will be used as an input into the GPIO pins on the Raspberry Pi 3 to find distance. The ground pins and Vcc pins on the HC-SR04 will be connected via the Vcc & GND pin on the RPI.

Output
GPIO-23: TRIGGER 

Input
GPIO-24: ECHO

The file will return a value in centimeters, can change for different units. 

Will need to follow circuit diagram posted in the SPOT Document for optimal results. 

Reference to the details above come from this website: https://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi


For Autonomous triggering, we use the command:
- nohup /home/pi/background_ping.sh

Step-by-step instructions for autonomous set up:
1. Make sure you run the setup script with each new Pi
2. Enjoy. ;)
