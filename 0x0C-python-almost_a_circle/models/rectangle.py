#!/usr/bin/python3
""

from models.base import Base


class Rectangle(Base):
    ""
    def intChecker(varName, val):
        if type(val) != int:
            raise TypeError("{} must be an integer".format(varName))
        elif val <= 0 and (varName == "width" or varName == "height"):
            raise ValueError("{} must be > 0".format(varName))
        elif val < 0 and (varName == "x" or varName == "y"):
            raise ValueError("{} must be >= 0".format(varName))
        else:
            return val

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = Rectangle.intChecker("width", width)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = Rectangle.intChecker("height", height)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = Rectangle.intChecker("x", x)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = Rectangle.intChecker("y", y)

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = Rectangle.intChecker("width", width)
        self.__height = Rectangle.intChecker("height", height)
        self.__x = Rectangle.intChecker("x", x)
        self.__y = Rectangle.intChecker("y", y)

    def area(self):
        return self.__width*self.__height

    def display(self):
        if self.__height != 0 and self.__width != 0:
            for y in range(self.__y):
                print()
            for h in range(self.__height):
                for x in range(self.__x):
                    print(" ", end="")
                for w in range(self.__width):
                    print("#", end="")
                if w == (self.__width - 1):
                    print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        attributes = ["id", "width", "height", "x", "y"]
        if args and len(args) > 0:
            for a in range(len(args)):
                setattr(self, attributes[a], args[a])
        else:
            for k in kwargs:
                # what if key is "foo" or "ha" (not an attribute)?
                setattr(self, k, kwargs.get(k))
