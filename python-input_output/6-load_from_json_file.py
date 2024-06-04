#!/usr/bin/python3
"""
This module represents creating an object
from a JSON file
"""

import json


def load_from_json_file(filename):
    """Method for creating python object file
    from JSON file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
