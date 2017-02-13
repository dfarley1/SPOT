#!/bin/bash
# If Raspberry Pi cannot find command, use line below:
# sudo apt-get install sshpass

sshpass -p 'raspberry'  scp /home/pi/SPOT/Cloud/test.json pi@10.0.0.1:~