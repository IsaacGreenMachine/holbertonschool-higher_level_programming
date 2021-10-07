#!/usr/bin/python3
[[print("{}{}".format(i, j), end=", ")
    for j in range(i+1, 10)] for i in range(0, 8)]
print("{}".format("89"))
