


#!/usr/bin/python
#
# bumper_final.py
# Measure distance using an ultrasonic module.
#
# Author : Erik Jung
# Date   : 01/29/2017

# -----------------------
# Import required Python libraries
# If libraries not installed into RPI devices, install them.
# Check README for more details.
# -----------------------

import RPi.GPIO as GPIO
import time

# -----------------------
# Define some functions
# -----------------------

def measure():
  # This function measures a distance
  GPIO.output(GPIO_TRIGGER, True)
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER, False)
  start = time.time()

  while GPIO.input(GPIO_ECHO)==0:
    start = time.time()

  while GPIO.input(GPIO_ECHO)==1:
    stop = time.time()

  elapsed = stop-start
  distance = (elapsed * 34300)/2

  return distance

def measure_average():
  # This function takes 3 measurements and
  # returns the average.
  distance1=measure()
  time.sleep(0.1)
  distance2=measure()
  time.sleep(0.1)
  distance3=measure()
  distance = distance1 + distance2 + distance3
  distance = distance / 3
  return distance

GPIO.setmode(GPIO.BCM)

TRIG = 11 
ECHO = 8

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


try:
	while True:
		distance = measure_average()
		print "Distance:",distance,"cm"
		time.sleep(1)

	except KeyboardInterrupt:
		GPIO.cleanup()





GPIO.cleanup()