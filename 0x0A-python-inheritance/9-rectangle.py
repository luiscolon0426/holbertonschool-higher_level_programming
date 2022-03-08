#!/usr/bin/python3
""" Full rectangle """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class rectangle """

    def __init__(self, width, height):

        BaseGeometry.integer_validator(self, "height", height)
        BaseGeometry.integer_validator(self, "width", width)

        self.__width = width
        self.__height = height

    def area(self):

        return self.__width * self.__height

    def __str__(self):

        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
