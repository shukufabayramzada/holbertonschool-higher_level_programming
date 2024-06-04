#!/usr/bin/python3
"""
This module represents retrieving a
dictionary representation of a Student instance
"""


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__

        if not isinstance(attrs, list):
            return self.__dict__

        filtered_dict = {}

        for attr in attrs:
            if isinstance(attr, str) and attr in self.__dict__:
                filtered_dict[attr] = self.__dict__[attr]

        return filtered_dict
