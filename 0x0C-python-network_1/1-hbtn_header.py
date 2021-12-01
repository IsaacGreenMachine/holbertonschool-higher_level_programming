#!/usr/bin/python3
from sys import argv
import urllib.request
req = urllib.request.Request(argv[1])
with urllib.request.urlopen(req) as response:
    html = response.read()
    print(response.headers.get("X-Request-Id"))
