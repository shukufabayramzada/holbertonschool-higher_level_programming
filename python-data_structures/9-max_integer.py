#!/usr/bin/python3
def max_integer(my_list=[]):
    for i in range(len(my_list)):
        for j in range(1, len(my_list)):
            if my_list[i] > my_list[j]:
                return my_list[i]
            else:
                return my_list[j]
