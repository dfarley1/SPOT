This is a README for the ping sensor setup.

GPIO Pins 23 and 24 are designated for operating the HC-SR04 ultrasonic ping sensor. Trigger will be used to enable the ping sensor for measuring distances, whereas echo will be used as an input into the GPIO pins on the Raspberry Pi 3 to find distance. The ground pins and Vcc pins on the HC-SR04 will be connected via the Vcc & GND pin on the RPI.

Output
GPIO-23: TRIGGER 

Input
GPIO-24: ECHO

The file will return a value in centimeters, can change for different units. 

Will need to follow circuit diagram posted in the SPOT Document for optimal results. 