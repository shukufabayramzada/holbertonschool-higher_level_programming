#!/usr/bin/python3
"""Module containing the definition of the Square class."""


class Square:
    """An class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the Square with a given size and position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the current size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print square"""
        if self.__size == 0:
            print("")
            return
        for _ in range(self.__position[1]):
            print("")
        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)

    @property
    def position(self):
        """Retrieve the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """ Set the value of the position tuple"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError(
                    "position must be a tuple of 2 positive integers"
            )
        self.__position = value
