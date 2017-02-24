PING_CHECKER="/home/pi/SPOT/Hardware/SensorNodes/ping_trigger.sh"
while [ 1 ]; do 
    $PING_CHECKER
    sleep 5
done
