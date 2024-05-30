#!/usr/bin/python3
"""
This module represents the checkinh about obj is an
instance of the given class or not
"""


def is_same_class(obj, a_class):
    """
    Return: the return value of isinstance
    for obj comparing with a_class
    """
    if isinstance(obj, a_class):
        return True
    return False
