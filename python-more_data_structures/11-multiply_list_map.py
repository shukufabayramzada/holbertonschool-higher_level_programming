#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = my_list.copy()
    result = list(map(lambda x: x * number, new_list))
    return result

