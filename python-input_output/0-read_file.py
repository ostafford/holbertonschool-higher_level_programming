#!/usr/bin/python3
"""
Reads and prints the content of a
specified file in UTF-8 encoding.
This function takes a filename as input,
opens the file in read mode with UTF-8 encoding,
reads the entire content of the file,
and prints it to the standard output.
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
