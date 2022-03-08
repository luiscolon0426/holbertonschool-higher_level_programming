#!/usr/bin/python3
""" inherits Basegeomtry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle """

    def __init__(self, width, height):
        """ Init the class"""
        BaseGeometry.integer_validator(self, "height", height)
        BaseGeometry.integer_validator(self, "width", width)

        self.__width = width
        self.__height = height
