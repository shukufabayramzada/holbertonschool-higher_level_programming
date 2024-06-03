#!/usr/bin/python3
"""
This module represents reads a text file
and prints its to stdout
"""


def read_file(filename=""):
    """Method for reads and
    printing it to stdout
    """
    with open(filename, 'r', encoding="utf-8") as f:
        f_contents = f.read()
        print(f_contents, end='')
