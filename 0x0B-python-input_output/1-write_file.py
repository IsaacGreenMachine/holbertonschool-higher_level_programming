#!/usr/bin/python3
"this is the module for write_file"


def write_file(filename="", text=""):
    "overwrites text to filename"
    with open(filename, "w+", encoding="utf-8") as f:
        return f.write(text)
