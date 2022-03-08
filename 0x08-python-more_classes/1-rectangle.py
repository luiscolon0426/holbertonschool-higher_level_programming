#!/usr/bin/python3
""" class Rectangle module """


class Rectangle:
    """ Define a rectangle """
    __width = None
    __height = None

    def __init__(self, width=0, height=0):
        """ define rectangle class witch width and height """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ Initializes height and width for rectangle class """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter method for width """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter method for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter method for height """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
