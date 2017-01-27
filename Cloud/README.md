Cloud Info:

1. Add MyKeyPair.pem from ~/SPOT/Cloud/MyKeyPair.pem to the ~/.ssh directory 
  - sudo cp ~/SPOT/Cloud/MyKeyPair.pem ~/.ssh
2. Change permissions of the MyKeyPair.pem
  - sudo chmod 600 ~/.ssh/MyKeyPair.pem

command to log in to EC2 instance
   ssh -i ~/.ssh/MyKeyPair.pem ec2-user@ec2-35-167-188-247.us-west-2.compute.amazonaws.com

