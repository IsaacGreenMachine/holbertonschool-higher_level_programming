#!/usr/bin/python3
"module for student class"


class Student:
    "defines a student with age, first and last name"
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return vars(self)
