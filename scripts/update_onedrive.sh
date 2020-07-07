#! /bin/bash

# Mount onedrive and detach
# https://www.linuxuprising.com/2018/07/how-to-mount-onedrive-in-linux-using.html
rclone --vfs-cache-mode writes mount onedrive: ~/OneDrive &

# Move to thesis directory
cd ~/Documents/thesis
# Clean
make cleaner
# Make
make

# Copy build to /tmp/ so can continue working on thesis whilst uploading
cp ~/Documents/thesis.pdf /tmp/

# Copy with rclone. -P shows progress of copy
rclone copy /tmp/thesis.pdf ~/OneDrive -P
