#!/usr/bin/python3
"""Module containing the definition of the Square class."""


class Square:
    """An class that defines a square"""

    def __init__(self, size=0):
        """Initialize the Square with a given size."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
