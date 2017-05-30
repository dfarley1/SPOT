#!/bin/bash
IMPORT_UUID="/home/pi/spot_log/uuid_file.txt"
CURRENT_UUID=`cat $IMPORT_UUID`
sudo hciconfig hci0 up
sudo hciconfig hci0 leadv 3
#sudo hcitool -i hci0 cmd 0x08 0x0008 1D 02 01 06 03 03 aa fe 15 16 aa fe 00 00  f7 82 6d a6 bc 5b 71 e0 89 3e
sudo hcitool -i hci0 cmd 0x08 0x0008 1e 02 01 06 03 03 aa fe 15 16 aa fe 00 00 $CURRENT_UUID
