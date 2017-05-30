import RPi.GPIO as GPIO

COLOR = 12
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(COLOR, GPIO.OUT)
GPIO.output(COLOR, False)


