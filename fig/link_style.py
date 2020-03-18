#! /usr/bin/env python3

"""Symlink the thesis style to the directory where matplotlib stores its styles."""

import os.path as path
import matplotlib as mpl
import subprocess

filename = "thesis.mplstyle"

link = path.join(mpl.__path__[0], 'mpl-data', 'stylelib', filename)

if not path.exists(link):
    target = path.join(path.dirname(path.abspath(__file__)), filename)
    subprocess.run(["ln", "-s", target, link])
    print("symlink created.")
else:
    print("symlink alread exists. no action.")

