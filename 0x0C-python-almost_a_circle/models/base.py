#!/usr/bin/python3
""" module that contains a Base class """

from os import path
import json


class Base:
    """ Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize the class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ import dict list to json """

        if list_dictionaries is None:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ json string rep of list obj to file """

        file = "{}.json".format(cls.__name__)

        file = "{}.json".format(cls.__name__)
        new = []
        with open(file, 'w') as f:
            if list_objs is None:
                f.write("[]")
            for obj in list_objs:
                new.append(obj.to_dictionary())
            f.write(cls.to_json_string(new))

    @staticmethod
    def from_json_string(json_string):
        lst = []
        if json_string is None:
            return lst
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes set """
        if cls.__name__ == "Rectangle":
            new_c = cls(1, 1)
        if cls.__name__ == "Square":
            new_c = cls(1)
        new_c.update(**dictionary)
        return (new_c)

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        new_lst = []
        empty = []
        file = "{}.json".format(cls.__name__)
        if path.isfile(file):
            with open(file, 'r') as f:
                new_lst = cls.from_json_string(f.read())
            for val in new_lst:
                empty.append(cls.create(**val))
            return empty

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ json string rep of list obj to file """

        file = "{}.csv".format(cls.__name__)
        new = []
        with open(file, 'w') as f:
            if list_objs is None:
                f.write("[]")
            for obj in list_objs:
                new.append(obj.to_dictionary())
            f.write(cls.to_json_string(new))

    @classmethod
    def load_from_file_csv(cls):
        """ Returns a list of instances """
        new_lst = []
        empty = []
        file = "{}.csv".format(cls.__name__)
        if path.isfile(file):
            with open(file, 'r') as f:
                new_lst = cls.from_json_string(f.read())
            for val in new_lst:
                empty.append(cls.create(**val))
            return empty
