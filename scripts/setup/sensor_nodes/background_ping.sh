PING_CHECKER="/home/pi/SPOT/CV/scripts/ping_trigger.sh"
while [ 1 ]; do 
    $PING_CHECKER
    sleep 5
done
