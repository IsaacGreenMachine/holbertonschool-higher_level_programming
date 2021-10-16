#!/usr/bin/python3
"module for student class"


class Student:
    "defines a student with age, first and last name"
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None and all(isinstance(x, str) for x in attrs):
            attList = []
            for v in vars(self):
                if v in self.__dict__:
                    attList.append(v)
            return attList
        else:
            return vars(self)
