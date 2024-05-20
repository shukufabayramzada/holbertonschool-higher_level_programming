#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    n = len(my_list)
    new_list = list(my_list)
    if idx < 0 or idx >= n:
        return new_list

    new_list[idx] = element
    return new_list
