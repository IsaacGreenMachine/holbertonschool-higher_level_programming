#!/usr/bin/python3
"Module for lookup method"


def lookup(obj):
    "Returns a list of all methods and attributes of obj"
    return(dir(obj))
