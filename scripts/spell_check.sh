#!/bin/bash

# To add words to dictionary append to internal/custom_spellings
# To add LaTex commands to ignore append to internal/ignore_tex

# Use luxurious 256 colour
function EXT_COLOUR () { echo -ne "\033[1;38;5;$1m"; }
NO_COLOUR="\033[0m"

# Directory of this script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Spell check all .tex files in chapters/ directory
files=$(find chapters/ . -maxdepth 1 -type f -name "*.tex")

echo -e "\n`EXT_COLOUR 75`SPELL CHECK RESULTS$NO_COLOUR\n"

for file in $files
do
    # List spelling mistakes
    mistakes=$(cat $file | 
               aspell list -t --conf=$DIR/../internal/ignore_tex \
                              --add-extra-dicts=$DIR/../internal/custom_spellings | \
               sort | uniq)

    # If there are no mistakes
    if [ -z "$mistakes" ]
    then
        echo -e "`EXT_COLOUR 34`$file$NO_COLOUR"
        echo -e "No spelling mistakes\n"
    else
        echo -e "`EXT_COLOUR 160`$file$NO_COLOUR"
        echo -e "$mistakes\n"
    fi
done
