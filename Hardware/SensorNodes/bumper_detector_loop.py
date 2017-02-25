import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 11 
ECHO = 8
  
print "Distance Measurement In Progress"
  
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
 
while(1):
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
     
    feet = 0.0328*distance
    print "Distance:",distance,"cm\tor",feet,"ft"

    time.sleep(0.5)
GPIO.cleanup()
