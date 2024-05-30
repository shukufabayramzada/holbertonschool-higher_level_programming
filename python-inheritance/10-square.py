#!/usr/bin/python3
"""
This module represents creating new class square
inherited from rectangle
"""

Rectangle = __import__('8-rectangle').Rectangle

class Square(Rectangle):
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

        super().__init__(size, size)

    def area(self):
        return self.__size**2

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
