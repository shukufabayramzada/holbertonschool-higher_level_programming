#!/usr/bin/python3
import json
"""
This module represents
returns the JSON representation of an object (string)
"""


def to_json_string(my_obj):
    """
    Convert te object to the json
    reprsenattion
    """
    return json.dumps(my_obj)
