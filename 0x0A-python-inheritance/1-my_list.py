#!/usr/bin/python3
"Module for MyList Class"


class MyList(list):
    "class for MyList"
    def print_sorted(self):
        super().sort()
        print(self)
