#!/bin/bash

# Specify location of ping_check program.
# NOTE: Make sure the file has executable rights
#       (i.e sudo chmod +x ./script)

# Hardware Scripts
PING_CHECKER="sudo python /home/pi/SPOT/Hardware/SensorNodes/bumper_distance_checker.py"
TRANSFER_SCRIPT="sudo runp /home/pi/SPOT/Cloud/testHttp.py sensor_POST"
TIMESTAMP_SCRIPT="sudo runp /home/pi/SPOT/Hardware/SensorNodes/occupied_since.py now"
EDDYSTONE_SCRIPT="sudo /home/pi/SPOT/scripts/setup/sensor_nodes/eddystone_test_setup.sh"
BLUETOOTH_SHUTOFF_SCRIPT = "sudo /home/pi/SPOT/scripts/setup/sensor_nodes/bluetooth_shutoff.sh"


# Reference for files
LOG_FILE="/home/pi/spot_log/license_log.txt"
TIME_FILE="/home/pi/spot_log/occupied_since.txt"
LOG_PIC="/home/pi/spot_log/license_log.png"
LOG_STATS="/home/pi/spot_log/license_log.json"


# Variables
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
	# Take photo
        raspistill -t 1 -o $LOG_PIC
        # Process the plate for user prefetch
        alpr -j $LOG_PIC >> $LOG_STATS

	# UPDATE FILE
	#echo $STATUS > $LOG_FILE

        # Activate beacon for this spot
        $EDDYSTONE_SCRIPT
    fi
    if [ $STATUS -eq $EMPTY ]; then
	# Turn off beacon
	$BLUETOOTH_SHUTOFF_SCRIPT
    fi

    # Update Log File
    # rm $LOG_FILE
    # echo $STATUS >> $LOG_FILE

    # Run timestamp script
    # runp occupied_since.py now
    sudo $TIMESTAMP_SCRIPT > $TIME_FILE
    OCCUPIED_SINCE = `cat $TIME_FILE`

    # Update Log File
    echo $STATUS > $LOG_FILE

    # Update Cloud with new status
    $TRANSFER_SCRIPT
fi
