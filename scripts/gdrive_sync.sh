#! /bin/bash

cd /home/jack/Documents/thesis
make cleaner
make

# Copy build to /tmp/ so can continue working on thesis whilst uploading
cp ~/Documents/thesis/thesis.pdf /tmp/

rclone sync /tmp/thesis.pdf gdrive3141: -P
