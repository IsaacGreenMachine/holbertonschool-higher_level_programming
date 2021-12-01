#!/usr/bin/python3
from sys import argv
from urllib import parse, request
import urllib
url = argv[1]
values = {"email": argv[2]}
data = parse.urlencode(values)
data = data.encode('ascii')
req = request.Request(url, data)
with request.urlopen(req) as response:
    html = response.read()