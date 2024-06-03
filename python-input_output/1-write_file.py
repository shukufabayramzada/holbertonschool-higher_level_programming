#!/usr/bin/python3
"""
This module represents writes a string to a text file
(UTF8) and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Write the text to the file
    and return the number of characters
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f_contents = f.write(text)
        return f_contents
