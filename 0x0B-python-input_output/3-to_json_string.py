#!/usr/bin/python3
"module for to_json_string"
import json


def to_json_string(my_obj):
    "returns my_obj as json string"
    return json.dump(my_obj)
