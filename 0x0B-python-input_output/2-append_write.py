#!/usr/bin/python3
""" appends a string at end of text file """


def append_write(filename="", text=""):
    """ append a sring """

    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
