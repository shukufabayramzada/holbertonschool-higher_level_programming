#!/usr/bin/python3
"""
This module represents working on Rectangle class
"""


class Rectangle:

    """An class that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the current width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value to the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the current height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value to the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
