#!/usr/bin/python3
"""

Function that says a name.

"""


def say_my_name(first_name, last_name=""):
    """
    class say_my_name
    """

    error1 = "first_name must be a string"
    error2 = "last_name must be a string"
    if type(first_name) is not str:
        raise TypeError(error1)
    if type(last_name) is not str:
        raise TypeError(error2)
    print("My name is {:s} {:s}".format(first_name, last_name))
