# bumper_detector_final.py
# Measure distance using an ultrasonic module
#
# Author : Erik Jung
# Date   : 01/26/2017

# -----------------------
# Import required Python libraries
# If libraries not installed into RPI devices, install them.
# Check README for more details.
# -----------------------
import time
import RPi.GPIO as GPIO

TRIG = 23

ECHO = 24

print "Distance Measurement In Progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)

print "Waiting For Sensor To Settle"

time.sleep(2)

GPIO.output(TRIG, True)

time.sleep(0.00001)

GPIO.output(TRIG, False)

while GPIO.input(ECHO)==0:
  pulse_start = time.time()

while GPIO.input(ECHO)==1:
  	pulse_end = time.time() 

pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 17150

distance = round(distance, 2)

print "Distance:",distance,"cm"

GPIO.cleanup()