#!/bin/bash

# The inbuilt spell-check of TexMaker leaves much to be desired.
# The spell-check checks the contents of commands such as \ref, \label, \cite,
# etc. which almost never contain meaningful words.

# To add words to dictionary append to inputs/custom_spellings
# To add LaTex commands to ignore append to inputs/ignore_tex

# Use luxurious 256 colour
function EXT_COLOUR () { echo -ne "\033[1;38;5;$1m"; }
NO_COLOUR="\033[0m"

# Directory of this script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# Files to spell check
files=$(find -type f -name "*.tex")

echo -e "\n`EXT_COLOUR 75`SPELL CHECK RESULTS$NO_COLOUR\n"
for file in $files
do
    # List spelling mistakes
    mistakes=$(cat $file | aspell list -t --conf=$DIR/ignore_tex \
               --add-extra-dicts=$DIR/custom_spellings | sort | uniq)
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
