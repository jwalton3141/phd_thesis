#! /bin/bash

module load bibtool

# Make a backup before messing anything up
cp references.bib references.bib.bak

# -r points to biblatex stuff
# -s sorts entries
bibtool -r /data/apps/bibtool/bibtool-2.67/usr/share/bibtool/biblatex.rsc -s -i references.bib -o out.bib

mv out.bib references.bib
