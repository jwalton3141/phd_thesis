#! /bin/bash

# Stick in crontab
# I should capture exit code of clone, try handle errors etc.
# but I'm trying hard not to procrastinate

# Allow notify-send to appear in user session when executed with cron
# https://askubuntu.com/a/346580/1037399
eval "export $(egrep -z DBUS_SESSION_BUS_ADDRESS /proc/$(pgrep -u $LOGNAME gnome-session)/environ)";

# Give user a heads up
notify-send "cron: thesis sync started"

# Work from /tmp/ to allow update to safely continue whilst I work
rm -rf /tmp/thesis
cp -r /home/jack/Documents/thesis /tmp/
cd /tmp/thesis

# Do a clean build
make cleaner && make

# Sync thesis to google drive
rclone sync /tmp/thesis/thesis.pdf gdrive3141: -P

notify-send "cron: thesis sync finished"
