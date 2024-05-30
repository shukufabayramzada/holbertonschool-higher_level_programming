#!/usr/bin/python3
"""
This module represents a class which inherits from list
"""


class MyList(list):
    """Class inherits from list"""
    def print_sorted(self):
        """Public instance method"""
        sorted_list = sorted(self)
        print(sorted_list)
