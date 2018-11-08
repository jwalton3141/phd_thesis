#!/bin/bash
# Open thesis if there is not an active ssh session
if ! [ -n "$SSH_CLIENT" ] && ! [ -n "$SSH_TTY" ]; then xdg-open thesis.pdf &> /dev/null & fi
