import RPi.GPIO as GPIO
import time
#from neopixel import *

# LED strip configuration:
LED_COUNT      = 24      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor$

# Define functions which animate LEDs in various ways.
#def colorWipe(strip, color, wait_ms=50):
#        """Wipe color across display a pixel at a time."""
#        for i in range(strip.numPixels()):
#                strip.setPixelColor(i, color)
#                strip.show()
#                time.sleep(wait_ms/1000.0)


# Create NeoPixel object with appropriate configuration.
#strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)

# Intialize the library (must be called once before other functions).
#strip.begin()

GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
car_distance = 1.5

TRIG = 23 
ECHO = 24
COLOR = 12
  
print "Distance Measurement In Progress"

# colorWipe(strip, Color(255,0,255))  
GPIO.setup(COLOR,GPIO.OUT)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

#GPIO,output(COLOR, False) 
GPIO.output(TRIG, False)
print "Waiting For Sensor To Settle"
time.sleep(0.05)
 
GPIO.output(TRIG, True)
time.sleep(0.001)
GPIO.output(TRIG, False)
pulse_start = 0;

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
time.sleep(0.05)
 
GPIO.output(TRIG, True)
time.sleep(0.001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO)==0:
  pulse_start = time.time()
 
while GPIO.input(ECHO)==1:
  pulse_end = time.time()

#GPIO.cleanup()
 
pulse_duration = pulse_end - pulse_start
 
distance_2 = pulse_duration * 17150

distance_2 = distance_2 * 0.032808

distance_2 = round(distance_2, 2)

print "Distance:",distance_2,"ft"

error = (abs((distance_1 - distance_2)) / distance_2) * 100

if error <= 10:
	if(distance_1 < car_distance):
		#colorWipe(strip, Color(0, 255, 0))
		GPIO.output(COLOR, False)
		GPIO.cleanup()
		exit(1)
GPIO.output(COLOR, True)
#coolorWipe(strip, Color(255,0,0))

GPIO.cleanup()
exit(0)
