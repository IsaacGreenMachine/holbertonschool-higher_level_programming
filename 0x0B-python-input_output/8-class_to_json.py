#!/usr/bin/python3
"This is the module for class_to_json"


def class_to_json(obj):
    "returns __dict__ for obj"
    return vars(obj)
