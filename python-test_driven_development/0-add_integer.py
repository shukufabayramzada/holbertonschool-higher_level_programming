#!/usr/bin/python3
"""This module defines addition of two float after converting to integers"""

def add_integer(a, b=98):
    """
    Returns an integer: the addition of a and b
    
    a and b must be first casted to integers if they are float

    Expected Errors:
    
    TypeError: a and b must be integers or floats, otherwise raise

    a TypeError exception with the message a must be an integer or b must be an integer
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer or float")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer or float")
    return (int(a) + int(b))
