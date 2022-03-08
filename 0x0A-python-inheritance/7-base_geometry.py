#!/usr/bin/python3
""" Module that contains the BaseGeometry class """


class BaseGeometry():
    """ Empty class """

    def area(self):
        """ Raises exception """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
