#!/bin/bash

# Add something add the top of this file which looks for ~.aspell.conf
# If it doesn't exist create it and add latex commands to ignore

GREEN='\033[0;32m'
NC='\033[0m'

for file in chapters/*.tex
do 
    printf "${GREEN}$file${NC}\n"
    cat $file | aspell list -t | sort | uniq
    echo -e "\n"
done
