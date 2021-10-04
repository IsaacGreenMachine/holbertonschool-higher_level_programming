#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a = a_dictionary.copy()
    a.setdefault(key, value)
    return a
