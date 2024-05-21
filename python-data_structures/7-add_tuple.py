#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    a1, a2 = tuple_a[:2]
    b1, b2 = tuple_b[:2]

    return (a1 + b1, a2 + b2)
