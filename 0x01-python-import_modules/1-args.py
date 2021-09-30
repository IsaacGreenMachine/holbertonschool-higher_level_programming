#!/usr/bin/python3
from sys import argv
if len(argv) < 2:
    print("0 arguments.")
elif len(argv) == 2:
    print("1 argument:")
    print("1: {}".format(argv[1]))
else:
    print("{} arguments:".format(len(argv) - 1))
    for arg in range(1, len(argv)):
        print("{}: {}".format(arg, argv[arg]))
