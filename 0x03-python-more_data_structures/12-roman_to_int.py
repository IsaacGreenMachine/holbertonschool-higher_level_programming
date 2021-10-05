#!/usr/bin/python3
def roman_to_int(roman_string):
    r = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 100}
    sum = 0
    i = 0
    a = r.get(roman_string[i])
    if i < len(roman_string) - 1:
        b = r.get(roman_string[i + 1])
    while i < len(roman_string) - 1:
        while i < len(roman_string) - 1 and a < b:
            sum -= r.get(roman_string[i])
            i += 1
            a = r.get(roman_string[i])
            if i < len(roman_string) - 1:
                b = r.get(roman_string[i + 1])
        while i < len(roman_string) - 1 and a >= b:
            sum += r.get(roman_string[i])
            i += 1
            a = r.get(roman_string[i])
            if i < len(roman_string) - 1:
                b = r.get(roman_string[i + 1])
    sum += r.get(roman_string[i])
    i += 1
    return sum
