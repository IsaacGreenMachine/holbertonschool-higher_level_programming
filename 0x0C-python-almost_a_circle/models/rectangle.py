#!/usr/bin/python3
"""
Defines a rectangle object that using superclass Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Instantiate the rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        returns the width property
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width property
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        returns the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        returns x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        sets x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        returns y
        """

        return self.__y

    @y.setter
    def y(self, value):
        """
        sets y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        calculates and returns area of rectangle
        """
        return (self.height * self.width)

    def display(self):
        """
        displays the rectangle with number signs
        """
        pound = "#"
        rectangle_string = ""
        for i in range(self.y):
            rectangle_string += "\n"
        for i in range(self.height):
            for i in range(self.x):
                rectangle_string += " "
            for j in range(self.width):
                rectangle_string += pound
            if i < self.height - 1:
                rectangle_string += "\n"
        print(rectangle_string)

    def __str__(self):
        """
        displays the info for the rectangle as a string
        """
        display = "[Rectangle] ({}) {}/{} - {}/{}"
        return (display.format(self.id, self.x, self.y, self.width,
                               self.height))

    def update(self, *args, **kwargs):
        """
        updates a rectangle object
        """
        dimensions = ['id', 'width', 'height', 'x', 'y']
        i = 0
        if args:
            for arg in args:
                setattr(self, dimensions[i], args[i])
                i += 1
        if kwargs:
            for key, arg in kwargs.items():
                setattr(self, key, arg)
