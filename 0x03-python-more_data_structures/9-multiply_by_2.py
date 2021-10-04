#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return dict(zip(a_dictionary.keys(), list(map(m, a_dictionary.values()))))


def m(x):
    return x * 2
