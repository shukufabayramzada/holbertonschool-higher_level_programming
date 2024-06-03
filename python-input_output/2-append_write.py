#!/usr/bin/python3
"""
This module represents appending a string at the end of the
text file
"""


def append_write(filename="", text=""):
    """
    Appends text to the file and
    return the number of characters
    """
    with open(filename, "a", encoding="utf-8") as f:
        f_contents = f.write(text)
        return f_contents
