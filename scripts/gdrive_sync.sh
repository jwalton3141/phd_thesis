#! /bin/bash

#https://askubuntu.com/a/346580/1037399
eval "export $(egrep -z DBUS_SESSION_BUS_ADDRESS /proc/$(pgrep -u $LOGNAME gnome-session)/environ)";


# I have done zero testing of this script...
# Stick in cron

notify-send "cron: thesis sync started"

# Move to thesis dir
cd /home/jack/Documents/thesis

# Do a clean build
make cleaner
make

# Copy build to /tmp/ so can continue working on thesis whilst uploading
cp ~/Documents/thesis/thesis.pdf /tmp/

# Sync thesis to google drive
rclone sync /tmp/thesis.pdf gdrive3141: -P

# Something something should capture exit code and condition output but ...
notify-send "cron: thesis sync finished"
