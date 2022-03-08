#!/usr/bin/python3
"""

Function that adds 2 integers.

"""


def add_integer(a, b=98):
    """
    Given two integers, return the sum.
    """

    if type(a) not in [float, int]:
        raise TypeError("a must be an integer")
    if type(b) not in [float, int]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
