#!/usr/bin/python3
import sys
if __name__ == "__main__":
    n = len(sys.argv)
    s = n - 1
    if s == 0:
        print("0 arguments.")
    elif s == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(s))

    for i in range(1, n):
        print("{}: {}".format(i, sys.argv[i]))
