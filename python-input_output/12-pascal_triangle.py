#!/usr/bin/python3
"""Module represents Pascal Triangle"""


def pascal_triangle(n):
    """Determine pascal triangle"""
    if n <= 0:
        return list

    current_list = [1]
    temp = []
    last_version = []

    for i in range(n):
        temp.append(1)
        for y in range(1, len(current_list)):
            temp.append(current_list[y] + current_list[y - 1])
        temp.append(1)
        last_version.append(current_list)
        current_list = temp
        temp = []
    return last_version
