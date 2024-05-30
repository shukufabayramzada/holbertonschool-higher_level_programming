#!/usr/bin/python3
"""
This module represents creating new class square
inherited from rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """Square class inherited from Rectangle class
    """
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

        super().__init__(size, size)
