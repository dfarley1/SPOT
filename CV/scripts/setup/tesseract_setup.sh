#!/bin/bash

# Install dependencies 
sudo apt-get install libpng12-dev libjpeg8-dev libjpeg-dev libtiff-dev zlib1g-dev
sudo apt-get install autoconf-archive automake autoconf
sudo apt-get install pkg-config libtool 

# Cascade training libraries
sudo apt-get install libicu-dev
sudo apt-get install libpango1.0-dev
sudo apt-get install libcairo2-dev
#----------------------------
ldconfig

# Get Tesseract source
cd /opt
git clone --depth 1 https://github.com/tesseract-ocr/tesseract.git
cd tesseract
./autogen.sh
./configure --enable-debug
LDFLAGS="-L/usr/local/lib" CFLAGS="-I/usr/local/include" make
make install
ldconfig

