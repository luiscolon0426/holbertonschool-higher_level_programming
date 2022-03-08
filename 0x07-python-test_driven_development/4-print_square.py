#!/usr/bin/python3
"""
Print Square
"""


def print_square(size):
    """
    Given a size, do a square
    """

    error1 = "size must be an integer"
    error2 = "size must be >= 0"
    if type(size) is not int:
        raise TypeError(error1)
    if size < 0:
        raise ValueError(error2)
    for i in range(size):
        print("#" * size)
