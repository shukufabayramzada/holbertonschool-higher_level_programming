#!/usr/bin/python3
def number_keys(a_dictionary):
    count = 0
    for key in a_dictionary:
        count += 1
        if isinstance(a_dictionary[key], dict):
            count += number_keys(a_dictionary[key])
    return count
