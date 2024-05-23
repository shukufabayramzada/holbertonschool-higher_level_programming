#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key not in a_dictionary:
        a_dictionary.setdefault(key, value)
    else:
        a_dictionary.update({'key': 'value'})
    return a_dictionary
            
