#!/usr/bin/python3
"""
This module represents if an object is an instance of,
or if the object is an instance of a class that inherited from
"""
def is_kind_of_class(obj, a_class):
    """
    Check for the case of being class
    """
    if type(obj) is a_class or isinstance(obj, a_class):
        return True
    return False

