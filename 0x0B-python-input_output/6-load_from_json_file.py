#!/usr/bin/python3
"module for load_from_json_file"
import json


def load_from_json_file(filename):
    "loads a .json file and returns an object"
    with open(filename, "r") as f:
        return json.loads(f.read())
