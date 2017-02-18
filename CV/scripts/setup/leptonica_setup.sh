#!/bin/bash

# Desc:	This script installs Leptonica v1.74.1

# Download all dependencies
apt-get install libpng12-dev libjpeg62 libtiff4
apt-get install libgif-dev
ldconfig

# Download. Change version type here
wget www.leptonica.com/source/leptonica-1.74.1.tar.gz
gunzip leptonica-1.74.1.tar.gz

# Unpack etc
tar -xf leptonica-1.74.1.tar
rm leptonica-1.74.1.tar

# Setup leptonica
mv ./leptonica-1.74.1 /opt
cd /opt/leptonica-1.74.1

# Build it (Option 3)
# mkdir build
# cd build
# cmake ..
# make

# Check the build
./configure
make
make install
make check

# END
echo "Finished...Leptonica setup over."
