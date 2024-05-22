#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return 0

    my_list.sort()
    total_sum = my_list[0]

    for i in range(1, len(my_list)):
        if my_list[i] != my_list[i - 1]:
            total_sum += my_list[i]

    return total_sum
