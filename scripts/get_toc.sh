#! /bin/bash

# Remove all lines except contents lines
sed '/defcounter\|boolfalse\|babel@toc/d' ../thesis.toc > toc
# Dinnae include subsections
sed -i '/subsection\|subsubsection/d' toc

# Remove everything except chapter and section and their title
sed -i 's/.*{chapter}{\\numberline {.*}\(.*\)}{.*}{.*}/\1 \&\t \\\\/g' toc
sed -i 's/.*{section}{\\numberline {.*}\(.*\)}{.*}{.*}/\t\t\& \1 \\\\/g' toc

# Print into tabular form
printf "\\\begin{table}\n\\\centering\n\\\begin{tabular}{@{}ll@{}}\n\\\toprule\n"
printf "Chapter & Section\\\\\\\\\midrule \n" 
cat toc
printf "\\\bottomrule\n\\\end{tabular}\n\\\end{table}"

rm toc
