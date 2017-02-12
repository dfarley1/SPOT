#!/bin/bash

sudo python /home/pi/SPOT/Hardware/SensorNodes/bumper_detector.py

scp /home/pi/test.json ec2-user@ec2-35-167-188-247.us-west-2.compute.amazonaws.com:~