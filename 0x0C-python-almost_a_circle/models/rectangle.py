#!/usr/bin/python3
""" Module that creates a class Rectangle """


from models.base import Base


class Rectangle(Base):
    """ class describing a rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializes the class """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the height. """
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the x attribute """
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """ sets the y attribute """
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns area value of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ comment."""
        if self.__y > 0:
            print(self.__y * "\n", end="")
        for _ in range(self.__height):
            for _ in range(self.__x):
                print(" ", end="")
            for _ in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ return the rectangle string. """

        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ comment. """
        if len(args) > 0:
            lst = ["id", "width", "height", "x", "y"]
            a = 0
            for arg in args:
                setattr(self, lst[a], arg)
                a += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns de dictionary. """
        return {
            "x": self.x,
            "width": self.width,
            "id": self.id,
            "height": self.height,
            "y": self.y,
        }
