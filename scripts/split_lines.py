#!/usr/bin/env python3

"""
Script to try insert a newline after every n-th character in a text file. If the n-th character is
in the middle of a word, insert the newline before that word.

Run as
    $ ./split_lines /path/to/file.txt /write/to/file.txt 79
Process multiple files with
    $ find `pwd` -type f -name "*.tex" -exec scripts/split_lines.py {} {} 79 \;
Alternatively run ./split_lines to be prompted for inputs
"""

import os
import sys

def load_and_split(file):
    with open(file, "r") as f:
        text = str(f.read())
    return text.splitlines()

def save(out, save_file):
    with open(save_file, "w") as f:
        f.write('\n'.join(out))

def split(line, out, every):
    every -= 1
    start = 0

    while start + every < len(line):
        end = start + every
        while line[end] != ' ':
            end -= 1
        out.append(line[start:end+1])
        start = end + 1

    out.append(line[start:])

def prompt_inputs():
    file = input("Path to file (relative or absolute): ")

    overwrite = input("Overwrite file? [y/n]: ")
    if overwrite == 'y':
        save_file = file
    else:
        save_file = input("Write new file to (default: {}.test): ".format(file)) or file + '.test'

    split_every = int(input("Split lines after every N characters (defaults to N=79): ") or 79)
    return file, save_file, split_every

def main():
    if len(sys.argv) == 4:
        file, save_file = sys.argv[1:3]
        split_every = int(sys.argv[3])
    else:
        file, save_file, split_every = prompt_inputs()

    # If not an absolute path append current working directory
    if file[0] != '/':
       file = os.getcwd() + '/' + file
    text = load_and_split(file)

    out = []
    for line in text:
        split(line, out, split_every)

    save(out, save_file)
    print("\nDone")

if __name__ == "__main__":
    main()
