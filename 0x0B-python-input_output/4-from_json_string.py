#!/usr/bin/python3
""" module that return an object PDS rep by JSON """


import json


def from_json_string(my_str):
    """ string to object method """
    return json.loads(my_str)
