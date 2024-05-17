#!/usr/bin/python3

import sys

if __name__ == "__main__":
    n = len(sys.argv)
    total_sum = 0
    if n == 1:
        print("no argument is provided")
    else:
        for i in range(1, n):
            total_sum += int(sys.argv[i])
        print("{}".format(total_sum))
