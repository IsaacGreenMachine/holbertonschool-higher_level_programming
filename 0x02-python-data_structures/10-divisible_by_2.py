#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return []
    else:
        a = []
        for i in my_list:
            if i < 0:
                two = -2
            else:
                two = 2
            if i % two == 0:
                a.append(True)
            else:
                a.append(False)
        return a
