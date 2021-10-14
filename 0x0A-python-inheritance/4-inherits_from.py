#!/usr/bin/python3
"This is the module for inherits_from"


def inherits_from(obj, a_class):
    "checks if object only inherits from class"
    return (isinstance(obj, a_class) and not (type(obj) == a_class))
