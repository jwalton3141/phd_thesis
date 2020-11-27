#! /bin/bash

# This script creates a clean build of my thesis and syncs the pdf with google
# drive. With this my supervisors can always have the latest build of my
# thesis, without having to make it themselves.

# The intention is for this script to be executed regularly with cron.

# https://stackoverflow.com/a/53598510/11021886
export XDG_RUNTIME_DIR=/run/user/$(id -u) 

notify-send Cron: "Thesis build & sync started"

# Work from /tmp/ so I can continue to work during sync
rm -rf /tmp/thesis
cp -r $HOME/Documents/thesis /tmp/
cd /tmp/thesis

# Do a clean build
make cleaner && make

if [ $? -eq 0 ]
then
    notify-send Cron: "Thesis build completed successfully"

    # Sync thesis to google drive (and onedrive)
    rclone sync /tmp/thesis/thesis.pdf gdrive3141: && \
    rclone sync /tmp/thesis/thesis.pdf onedrivencl: \
        && notify-send Cron: "Thesis sync completed successfully" \
        || notify-send Cron: "Thesis sync failed"

    # Clean up after succesful build
    rm -rf /tmp/thesis
else
    notify-send Cron: "Thesis build failed"
    # Don't clean up after build fail (logs and output useful for debug)
fi

