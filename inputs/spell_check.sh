#!/bin/bash

# The inbuilt spell-check of TexMaker leaves much to be desired.
# The spell-check checks the contents of commands such as \ref, \label, \cite,
# etc. which almost never contain meaningful words.

# To add words to dictionary append to inputs/custom_spellings
# To add LaTex commands to ignore append to inputs/ignore_tex

# Define escape codes for easier print formatting
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

# Directory of this script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

printf "\n${RED}SPELL CHECK RESULTS${NC}\n\n"

for file in chapters/*.tex
do 
    printf "${GREEN}$file${NC}\n"
    cat $file | aspell list -t --conf=$DIR/ignore_tex --add-extra-dicts=$DIR/custom_spellings | sort | uniq
    echo -e "\n"
done
