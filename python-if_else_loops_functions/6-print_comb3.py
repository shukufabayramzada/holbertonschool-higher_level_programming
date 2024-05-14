#!/usr/bin/python3
for n in range(9):
    for i in range(1, 10):
        if i != n and n < i:
            print("{}{}".format(n, i), end=", " if (n * 10 + i) < 89 else "\n")
