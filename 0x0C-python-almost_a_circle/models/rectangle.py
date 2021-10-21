#!/usr/bin/python3
"""this module contains a rectangle"""


from models.base import Base


class Rectangle(Base):
    """Child of Base with width, height, x, and y"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle init. uses Base init. validates values and sets them."""
        super().__init__(id)
        self.__width = Rectangle.intChecker("width", width)
        self.__height = Rectangle.intChecker("height", height)
        self.__x = Rectangle.intChecker("x", x)
        self.__y = Rectangle.intChecker("y", y)

    def intChecker(varName, val):
        """Checks if val is an int and above 0."""
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
        """returns width"""
        return self.__width

    @width.setter
    def width(self, width):
        """validates width is int and sets it"""
        self.__width = Rectangle.intChecker("width", width)

    @property
    def height(self):
        """returns height"""
        return self.__height

    @height.setter
    def height(self, height):
        """validates height is int and sets it"""
        self.__height = Rectangle.intChecker("height", height)

    @property
    def x(self):
        """returns x"""
        return self.__x

    @x.setter
    def x(self, x):
        """validates x is int and sets it"""
        self.__x = Rectangle.intChecker("x", x)

    @property
    def y(self):
        """returns y"""
        return self.__y

    @y.setter
    def y(self, y):
        """validates y is int and sets it"""
        self.__y = Rectangle.intChecker("y", y)

    def area(self):
        """returns area of rectangle"""
        return self.__width*self.__height

    def display(self):
        """prints self in hashtags with x, y offset"""
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
        """returns Rectangle def when print() or str() used"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """updates and validates (setattr) attributes of instance"""
        attributes = ["id", "width", "height", "x", "y"]
        if args and len(args) > 0:
            for a in range(len(args)):
                setattr(self, attributes[a], args[a])

        else:
            for k in kwargs:
                if k in attributes:
                    setattr(self, k, kwargs.get(k))

    def to_dictionary(self):
        """returns dict representaiton of object"""
        attributes = ["id", "width", "height", "x", "y"]
        d = {}
        for a in attributes:
            d.update({a: getattr(self, a)})
        return d
