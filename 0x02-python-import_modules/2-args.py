#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    idx = 1
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("{} argument:".format(len(argv) - 1))
    else:
        print("{} arguments:".format(len(argv) - 1))
    while idx + 1 < len(argv) + 1:
        print("{}: {}".format(idx, argv[idx]))
        idx = idx + 1
