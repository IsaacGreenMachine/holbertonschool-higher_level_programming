#!/usr/bin/python3
def pow(a, b):
    c = 1
    if b == 0:
        return c
    for n in range(abs(b)):
            c *= a
    if b > 0:
        return c
    else:
        return (1/c)
