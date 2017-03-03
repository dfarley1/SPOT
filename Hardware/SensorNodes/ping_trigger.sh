#!/bin/bash

# Specify location of ping_check program.
# NOTE: Make sure the file has executable rights
#       (i.e sudo chmod +x ./script)
#PING_CHECKER="/home/pi/SPOT/CV/scripts/photo_triggers/test_occupied"
PING_CHECKER="python /home/pi/SPOT/Hardware/SensorNodes/bumper_distance_checker.py"
TRANSFER_SCRIPT="runp /home/pi/SPOT/Cloud/testHttp.py sensor_POST"
#TRANSFER_SCRIPT="runp /home/pi/SPOT/Cloud/testHttp.py testPOST:$STATUS"
#TRANSFER_SCRIPT="/home/pi/SPOT/Cloud/testPost.sh"
LOG_FILE="/home/pi/spot_log/license_log.txt"
LOG_PIC="/home/pi/spot_log/license_log.png"
LOG_STATS="/home/pi/spot_log/license_log.json"
EDDYSTONE_SCRIPT="/home/pi/SPOT/scripts/setup/sensor_nodes/eddystone_test_setup.sh"

PHOTO_TRIG=1
EMPTY=0
OCCUPIED=1

# Run script to check for output
# python ping_check
$PING_CHECKER
STATUS=$?
LAST_STATUS=`cat $LOG_FILE`

# Check for event
if [ $STATUS -ne $LAST_STATUS ]; then
    # A car has entered the spot, take a picture
    if [ $STATUS -eq $OCCUPIED ]; then

        raspistill -t 1 -o $LOG_PIC
        # Process the plate for user prefetch
        alpr -j $LOG_PIC >> $LOG_STATS

        # Activate beacon for this spot
        $EDDYSTONE_SCRIPT

    	# Send to gateway
        # Insert transmission script HERE

        $TRANSFER_SCRIPT
    fi
    # Update the log file
    rm $LOG_FILE
    echo $STATUS >> $LOG_FILE
fi
