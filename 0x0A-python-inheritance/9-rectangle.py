#!/usr/bin/python3
"This is the module for BaseGeometry"
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    "raises Exception"
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        if self.__width and self.__height:
            return "[Rectangle] {}/{}".format(self.__width, self.__height)
