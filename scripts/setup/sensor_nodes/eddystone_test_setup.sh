#!/bin/bash

sudo hciconfig hci0 up
sudo hciconfig hci0 leadv 3
sudo hcitool -i hci0 cmd 0x08 0x0008 1D 02 01 06 03 03 aa fe 15 16 aa fe 00 00 0a 2c 72 59 b8 04 17 ff 9d ff 01 02 03 04 05 06
