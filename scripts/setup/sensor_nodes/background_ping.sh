PING_CHECKER="/home/pi/SPOT/Hardware/SensorNodes/ping_trigger.sh"
while [ 1 ]; do 
    sudo $PING_CHECKER
    sleep 5
done
