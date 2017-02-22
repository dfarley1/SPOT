import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

car_distance = 2

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
 
distance_1 = pulse_duration * 17150

distance_1 = distance_1 * 0.032808
 
distance_1 = round(distance_1, 2)

print "Distance:",distance_1,"ft"

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

GPIO.cleanup()
 
pulse_duration = pulse_end - pulse_start
 
distance_2 = pulse_duration * 17150

distance_2 = distance_2 * 0.032808

distance_2 = round(distance_2, 2)

print "Distance:",distance_2,"ft"

error = ((distance_1 - distance_2) / distance_2) * 100

if error <= 10:
	if(distance_1 < car_distance):
		exit(1)

exit(0)
