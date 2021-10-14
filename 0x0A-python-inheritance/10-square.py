#!/usr/bin/python3
"This is the module for BaseGeometry"
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    "raises Exception"
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2
