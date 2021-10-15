#!/usr/bin/python3
"Module for read_file"


def read_file(filename=""):
    "reads a file and prints to stdout"
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
