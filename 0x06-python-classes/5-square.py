#!/usr/bin/python3
""" Module with the class Square """


class Square:
    """ Square Defined """
    __size = None

    def __init__(self, size=0):
        """ Docstring of __init___ method

        Args:
            size (int): size from main to be displayed
        """
        self.__size = size
        """ int: Docstring *after* attribute, with type specified """

    @property
    def size(self):
        """ Docstring of size """
        return self.__size
        """ returns the size attribute with value """

    @size.setter
    def size(self, value):
        """ Docstring of size

        Args:
            value (int): Contains size from __size attribute
        """
        if (type(value) != int):
            raise TypeError("size must be an integer")
        if (self.__size < 0):
            raise ValueError("size must be >= 0")
        self.__size = value
        """ set size """

    def area(self):
        """ Docstring of area """
        return self.__size * self.__size
        """ size squared """

    def my_print(self):
        """ Docstring of my_print printer """
        if (self.__size == 0):
            print()
        else:
            for x in range(self.__size):
                print("#" * self.__size)
