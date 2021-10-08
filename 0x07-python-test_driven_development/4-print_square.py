#!/usr/bin/python3
"""This is the module for printing a square"""


def print_square(size):
    """prints a size x size square."""
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for i in range(size):
        [print("#", end="") for i in range(size)]
        print()
