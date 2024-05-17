#!/usr/bin/python3
import sys
n = len(sys.argv)
s = n - 1
if s == 0:
    print("0 arguments.")

for i in range(1, s):
    print("{} argument:".format(i))
    print("{}: {}".format(i, sys.argv[i]))
