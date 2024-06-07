#!/usr/bin/env python3

"""
This module representing reading data from one format (CSV)
and converting it into another format (JSON) using serialization
techniques.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        json_data = json.dumps(data, indent=4)

        with open('data.json', 'w') as f:
            f.write(json_data)

        return True
    except FileNotFoundError:
        print("File not found.")
        return False