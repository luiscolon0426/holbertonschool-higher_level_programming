#!/usr/bin/python3
""" a basic class """


class Student:
    """ student class """

    def __init__(self, first_name, last_name, age):
        """ ini the students """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ ret dict """
        if attrs is None:
            return self.__dict__

        Newdict = {}
        for a in attrs:
            try:
                Newdict[a] = self.__dict__[a]
            except:
                pass
        return Newdict
