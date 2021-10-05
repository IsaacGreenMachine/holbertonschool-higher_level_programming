#!/usr/bin/python3
"""creates a class is for a square"""


class Square:
    """Here it is. Here's the square."""
    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise ValueError("size must be an integer")

    def area(self):
        return(self.__size ** 2)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise ValueError("size must be an integer")

    def my_print(self):
        for i in range(self.__size):
            [print("#", end="") for i in range(self.__size)]
            print()
