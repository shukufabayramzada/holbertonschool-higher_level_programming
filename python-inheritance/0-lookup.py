#!/usr/bin/python3
"""
  This module represents printing the list of
  available attributes and methods of an object
"""


def lookup(obj):
    """
    Return: list of all atrributes and methods of an object
    """
    return dir(obj)
