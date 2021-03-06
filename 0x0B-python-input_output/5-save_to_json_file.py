#!/usr/bin/python3
"module for save_to_json_file"
import json


def save_to_json_file(my_obj, filename):
    "saves my_obj as json string to filename"
    with open(filename, "w+") as f:
        f.write(json.dumps(my_obj))
