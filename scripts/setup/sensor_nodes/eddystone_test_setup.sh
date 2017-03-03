#!/bin/bash

sudo hciconfig hci0 up
sudo hciconfig hci0 leadv 3

#Broadcasts to spdspot.com
#sudo hcitool -i hci0 cmd 0x08 0x0008 16 02 01 06 03 03 aa fe 0e 16 aa fe 10 00 03 73 64 70 73 70 6f 74 07 00 00 00 00 00 00 00 00 00

#Broadcasts to webgazer.org
#sudo hcitool -i hci0 cmd 0x08 0x0008 17 02 01 06 03 03 aa fe 0f 16 aa fe 10 00 03 77 65 62 67 61 7a 65 72 08 00 00 00 00 00 00 00 00

#Attempting to bradcast using UID
 sudo hcitool -i hci0 cmd 0x08 0x0008 1e 02 01 06 03 03 aa fe 15 16 aa fe 00 e7 00 01 02 03 04 05 06 07 08 09 01 02 03 04 05 06

#sudo hcitool -i hci0 cmd 0x08 0x0008 17 02 01 06 03 03 aa fe 0f 16 aa fe 00 0x00 0x584B930E3D99416E615D 0x123456123456 00 00


#Website to generate the payload of url: http://yencarnacion.github.io/eddystone-url-calculator/
