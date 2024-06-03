#!/usr/bin/python3
"""
This module represents
returning an object reprsented by a JSON
string
"""


import json


def from_json_string(my_str):
    """
    Return the object reprsenented
    by a JSON string
    """
    return json.loads(my_str)
