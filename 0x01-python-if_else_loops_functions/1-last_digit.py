#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    x = number % -10
else:
    x = number % 10
if x == 0:
    print("Last digit of {} is 0 and is 0".format(number))
elif x < 6:
    print("Last digit of {} is {}".format(number, x), end=" ")
    print("and is less than 6 and not 0")
else:
    print("Last digit of {} is {}".format(number, x), end=" ")
    print("and is greater than 5")
