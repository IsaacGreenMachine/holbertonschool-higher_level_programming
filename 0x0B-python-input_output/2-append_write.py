#!/usr/bin/python3
"this is the module for append_write"


def append_write(filename="", text=""):
    "appends to the end of a file"
    with open(filename, "a+", encoding="utf-8") as f:
        return f.write(text)
