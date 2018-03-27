#!/bin/bash

RED='\033[0;32m'
NC='\033[0m'

for file in chapters/*
do 
    printf "${RED}$file${NC}\n"
    cat $file | aspell list -t | sort | uniq
    echo -e "\n"
done
