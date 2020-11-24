#! /bin/bash

# Stick in crontab
# I should capture exit code of clone, try handle errors etc.
# but I'm trying hard not to procrastinate

# Give user a heads up
# https://stackoverflow.com/a/53598510/11021886
XDG_RUNTIME_DIR=/run/user/$(id -u) notify-send Cron: "thesis sync started"

# Work from /tmp/ to allow update to safely continue whilst I work
rm -rf /tmp/thesis
cp -r /home/jack/Documents/thesis /tmp/
cd /tmp/thesis

# Do a clean build
make cleaner && make

# Sync thesis to google drive
rclone sync /tmp/thesis/thesis.pdf gdrive3141: -P

XDG_RUNTIME_DIR=/run/user/$(id -u) notify-send Cron: "thesis sync finished"
