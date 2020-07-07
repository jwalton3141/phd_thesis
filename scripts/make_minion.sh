#! /bin/bash

# Install MinionPro locally. Does not require root.

# REQUIRES:
#    1. LCDF-typetools (if root: `$ sudo apt install lcdf-typetools`,
#                       if not root: build locally)
#    2. Recent TeXLive or MiKTex install

FPDIR=/tmp/FontPro
FONT=MinionPro
# TEXMFLOCAL or TEXMFHOME. TEXMFLOCAL *will* require root.
INSTALLDIR=TEXMFLOCAL

# Clone FontPro project
git clone https://github.com/sebschub/FontPro.git $FPDIR

# Directory for sources
mkdir -p $FPDIR/otf

# Download sources
curl -fLo $FPDIR/otf/minion-pro.zip \
    https://www.wfonts.com/download/data/2016/05/26/minion-pro/minion-pro.zip

# Unzip sources
unzip $FPDIR/otf/minion-pro.zip -d $FPDIR/otf/
# Delete extras
rm $FPDIR/otf/*{png,txt,zip}

# Move to project for make / install
cd $FPDIR

# Make
./scripts/makeall $FONT 

# Install
if [ $INSTALLDIR = TEXMFLOCAL ]; then
   sudo ./scripts/install "$(kpsewhich -expand-var='$TEXMFLOCAL')"
   sudo updmap-sys --enable Map=$FONT.map
else
   ./scripts/install "$(kpsewhich -expand-var='$TEXMFHOME')"
   updmap-user --enable Map=$FONT.map
fi

