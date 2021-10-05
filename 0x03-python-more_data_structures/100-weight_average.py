#!/usr/bin/python3
def weight_average(my_list=[]):
    total = 0
    denom = 0
    for i in my_list:
        total += i[0] * i[1]
        denom += i[1]
    if denom != 0:
        return total/denom
    else:
        return total
