#! /bin/bash

# Install MinionPro locally. Does not require root.
# Font will be installed to TEXMFHOME
# TEXMFHOME can be queried with `$ kpsewhich -expand-var='$TEXMFHOME'`

# REQUIRES:
#    1. LCDF-typetools (if root: `$ sudo apt install lcdf-typetools`,
#                       if not root: build locally)
#    2. Recent TeXLive or MiKTex install

FPDIR=/tmp/FontPro
FONT=MinionPro
CWD=$(pwd)

# Clone FontPro project
git clone https://github.com/sebschub/FontPro.git $FPDIR

# Directory for sources
mkdir -p $FPDIR/otf

# Download sources
curl -fLo $FPDIR/otf/minion-pro.zip \
    https://www.wfonts.com/download/data/2016/05/26/minion-pro/minion-pro.zip

# Unzip sources
unzip $FPDIR/otf/minion-pro.zip -d $FPDIR/otf/

# Move to project for make / install
cd $FPDIR
# Make fonts
./scripts/makeall $FONT --quiet
# Install fonts
./scripts/install $(kpsewhich -expand-var='$TEXMFHOME')
# Move back
cd $CWD

# Update user font map
updmap-user --enable Map=$FONT.map
