#!/usr/bin/python3

"""
This module represents  adding new atrribute to the object
if it`s possible
"""


def add_attribute(obj, key, value):
    """
    Adds new attribute if it is possible
    """
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")
    obj.__dict__[key] = value
