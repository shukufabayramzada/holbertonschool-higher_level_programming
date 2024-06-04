#!/usr/bin/python3
"""This module represents adds all arguments to a Python list,
and then save them to a json reprsented file
"""


import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

loads = load_from_json_file('add_item.json')
save_to_json_file((loads + sys.argv[1:]), 'add_item.json')
