#!/usr/bin/python3
"This is the module for is_same_class"


def is_same_class(obj, a_class):
    "Detecs if obj is in class"
    return type(obj) == a_class
