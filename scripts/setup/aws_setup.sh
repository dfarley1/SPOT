#!/bin/bash

sudo cp ~/SPOT/Cloud/MyKeyPair.pem ~/.ssh
sudo chmod 600 ~/.ssh/MyKeyPair.pem

#ssh -i ~/.ssh/MyKeyPair.pem ec2-user@ec2-35-167-188-247.us-west-2.compute.amazonaws.com