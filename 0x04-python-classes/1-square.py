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
