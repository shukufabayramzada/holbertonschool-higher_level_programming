#!/usr/bin/python3
"""
This module represents if an object is an instance
of a class that inherited from
"""


def inherits_from(obj, a_class):
    """
    Check for the case of being class
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
