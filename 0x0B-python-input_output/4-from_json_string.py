#!/usr/bin/python3
"module for from_json_string"
import json


def from_json_string(my_str):
    "converts json string to python object"
    return json.loads(my_str)
