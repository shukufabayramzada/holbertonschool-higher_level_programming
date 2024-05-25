#!/usr/bin/python3
"""Module containing the definition of the Square class."""


class Square:
    """An class that defines a square"""

    def __init__(self, size):
        """Initialize the Square with a given size."""
        try:
            if isinstance(size, int) and size > 0:
                self.__size = size
        except ValueError:
            print("size must be >= 0")
        except TypeError:
            print("size must be an integer")
