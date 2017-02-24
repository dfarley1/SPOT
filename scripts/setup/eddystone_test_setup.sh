#!/bin/bash

sudo hciconfig hci0 up
sudo hciconfig hci0 leadv 3
sudo hcitool -i hci0 cmd 0x08 0x0008 16 02 01 06 03 03 aa fe 0e 16 aa fe 10 00 03 73 64 70 73 70 6f 74 07 00 00 00 00 00 00 00 00 00

#Website to generate the payload of url: http://yencarnacion.github.io/eddystone-url-calculator/
