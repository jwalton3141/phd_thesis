#! /bin/bash

# Identify figures in fig/ which aren't included anywhere 

for chapter in $(ls chapters/*tex | xargs -n 1 basename)
do
    echo Checking chapter: ${chapter}...

    used_figs=($(sed -n -E "s/.*includegraphics(\[[^}]*\])*\{([^}]*)\}.*/\2/p" chapters/${chapter}))
    all_figs=($(cd fig/${chapter%.*} && find -type f -regex ".*jpg\|.*pdf\|.*png\|.*gif" -printf "%P\n"))

    for fig in ${all_figs[@]}
    do
        if ! $(echo ${used_figs[@]} | grep -q -P ${fig}); then
            echo "    ${fig} unused"
        fi
    done
done

