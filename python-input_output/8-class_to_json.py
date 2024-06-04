#!/usr/bin/python3
"""
This module represents a function that returns
the dictionary description with simple data structure
for JSON serialization of an object
"""


def class_to_json(obj):
    json_obj = {}

    for key, value in obj.__dict__.items():
        json_obj[key] = value

    return json_obj

    # Without importing module it can be written as
    # in the following way by imporrting json
    # return json.dumps(obj.__dict__)
