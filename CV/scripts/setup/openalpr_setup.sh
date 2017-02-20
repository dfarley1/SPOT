#!/bin/bash

# Install critical dependencies
./opencv_setup.sh
./leptonica_setup.sh
./tesseract_setup.sh

# Get necessary dependencies
apt-get install libpng12-dev libjpeg62-dev libtiff5-dev zlib1g-dev liblog4cplus-dev libcurl4-gnutls-dev
apt-get install build-essential
apt-get install autoconf automake libtool
apt-get install git-core
apt-get install cmake
ldconfig

# Get source files
cd /opt
git clone https://github.com/openalpr/openalpr.git
cd openalpr

# Set cmake settings
TOK="# Describe location of dependencies (0xDC)\n"
TOK=${TOK}"SET(OpenCV_DIR \"/opt/opencv/release\")\n"
TOK=${TOK}"SET(Tesseract_DIR \"/opt/tesseract\")\n"
echo -e "$TOK\n$(cat ./src/CMakeLists.txt)" > ./src/CMakeLists.txt

# Build it
cd src
cmake ./
make
ldconfig

# End installation
echo "Finished...Openalpr installed."
