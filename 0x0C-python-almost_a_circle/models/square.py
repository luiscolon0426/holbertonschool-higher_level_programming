#!/usr/bin/python3
""" module that contains a square that inherits from class Rectangle """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Define Square """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ return size attribute """
        return self.width

    @size.setter
    def size(self, value):
        """ comment """
        self.width = value
        self.height = value

    def __str__(self):
        """ method to returns [Rectangle] """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    def update(self, *args, **kwargs):
        """ update class Square """
        lst = ['id', 'size', 'x', 'y']
        if args:
            for i in range(len(args)):
                setattr(self, lst[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ comment """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
