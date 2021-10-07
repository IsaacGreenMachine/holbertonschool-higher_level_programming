#!/usr/bin/python3
for i in range(100):
    if i == 99:
        sep = "\n"
    else:
        sep = ", "
    print("{}{}".format(i, sep), end="")
