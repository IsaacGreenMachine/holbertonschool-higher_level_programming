#!/usr/bin/python3
"module for add_item"
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
try:
    oldJson = load_from_json_file("add_item.json")
except FileNotFoundError:
    oldJson = []
save_to_json_file(oldJson + sys.argv[1:], "add_item.json")
