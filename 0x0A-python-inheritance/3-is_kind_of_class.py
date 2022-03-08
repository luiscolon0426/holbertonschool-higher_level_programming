#!/usr/bin/python3
""" usage of type """


def is_kind_of_class(obj, a_class):
    """ check wether an object is the same type of another """

    if isinstance(obj, a_class):
        return True
    else:
        return False
