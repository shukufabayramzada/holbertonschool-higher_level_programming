#!/usr/bin/python3

import sys
import importlib

if __name__ == "__main__":
    n = len(sys.argv)
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    calculator_1 = importlib.import_module('calculator_1')

    if n != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if sys.argv[2] == "+":
            print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
        elif sys.argv[2] == "-":
            print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
        elif sys.argv[2] == "*":
            print("{} + {} = {}".format(a, b, calculator_1.mul(a, b)))
        elif sys.argv[2] == "/":
            print("{} + {} = {}".format(a, b, calculator_1.div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        exit(0)
