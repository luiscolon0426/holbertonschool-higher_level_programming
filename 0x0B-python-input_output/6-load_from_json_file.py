#!/usr/bin/python3
""" create an Object from json file"""

import json


def load_from_json_file(filename):
    """ creates an object """
    with open(filename) as file:
        objeto = json.load(file)
        return objeto
