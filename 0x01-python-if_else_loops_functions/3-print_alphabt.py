#!/usr/bin/python3
'''
for i in range(97, 123):
    if chr(i) != 'q' and chr(i) != 'e':
        print("{}".format(chr(i)), end="")
'''
[print("{}".format(chr(a)), end="")
    for a in range(97, 123) if a != 101 and a != 113]
