#!/usr/bin/python3
"""This module represent printing square with #"""


def print_square(size):
    """
       Function that prints # in size of square

       Return: Square

       Args:
         size (length of square)

       Possible Errors:
         TypeError - based on size type
         ValueError - based on value of size
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
