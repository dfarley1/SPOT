#!/bin/bash

DIST_SCRIPT=""
PHOTO_SCRIPT=""
DIST_STATUS="/home/pi/spot_status.txt"

YES_TRIG="1"
NO_TRIG="0"

python $SCRIPT_PATH
if [ "$?" -eq "$YES_TRIG"} ]; then
    # Only respond to events
    LAST_STATUS=`cat $DIST_STATUS`
    if [ "$LAST_STATUS" -eq "$NO_TRIG"]; then    
        echo "Object detected. Taking a photo..."
        chmod +x DIST_SCRIPT
    fi
else if [ "$?" -eq "$NO_TRIG"]
    
fi

