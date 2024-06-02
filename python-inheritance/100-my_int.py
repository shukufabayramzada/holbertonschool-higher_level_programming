#!/usr/bin/python3
"""
This module represents creating an instance of int class
"""


class MyInt(int):
    """Creating with expectations"""

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
