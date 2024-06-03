#!/usr/bin/python3
"""
This module represents
writes an Object to a text file, using a JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """
    write object to the file
    using json representation
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return json.dump(my_obj, f)
