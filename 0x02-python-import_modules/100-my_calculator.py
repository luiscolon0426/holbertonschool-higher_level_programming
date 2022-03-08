#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if (len(argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]

    if op == "+":
        r = add(a, b)
    elif op == "-":
        r = sub(a, b)
    elif op == "*":
        r = mul(a, b)
    elif op == "/":
        r = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{:d} {:s} {:d} = {:d}".format(a, op, b, r))
