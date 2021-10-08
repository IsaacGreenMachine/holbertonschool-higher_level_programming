#!/usr/bin/python3
"""This is the module for printing indented trext"""


def text_indentation(text):
    """This for prints text w/ a space in between"""
    if type(text) is None or type(text) != str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == " ":
            if i != 0 and text[i - 1] in ['.', '?', ':']:
                pass
            else:
                print("{}".format(text[i]), end="")
        else:
            print("{}".format(text[i]), end="")
        if text[i] in ['.', '?', ':']:
            print("{}".format('\n' * 2), end="")
    print()
