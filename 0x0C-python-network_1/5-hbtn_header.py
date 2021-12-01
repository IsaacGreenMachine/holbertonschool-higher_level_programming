#!/usr/bin/python3
"""sends request to URL and displays the X-Request-Id"""
import requests
import sys
r = requests.get(sys.argv[1])
print(r.headers.get("X-Request-Id"))
