#!/usr/bin/python3
n = 1
for i in range(10):
    for j in range(i + 1, 10):
        if i != 8 or j != 9:
            print(i, j, sep="", end=", ")
        else:
            print(i, j, sep="")
