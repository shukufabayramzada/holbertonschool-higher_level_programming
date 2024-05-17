#!/usr/bin/python3

import sys

if __name__ == "__main__":
    n = len(sys.argv)
    s = n - 1
    if s == 0:
        print("no argument is provided")
    elif s == 1:
        print("{}".format(int(sys.argv[1])))
    else:
        for i in range(1, s):
            add = 0
            x = int(sys.argv[i])
            add += x
            print("{}".format(add))
