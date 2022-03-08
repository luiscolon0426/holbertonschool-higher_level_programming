#!/usr/bin/python3
""" module that reads a text file """


def read_file(filename=""):
    """ read text file """

    with open(filename) as file:
        print(file.read(), end="")
