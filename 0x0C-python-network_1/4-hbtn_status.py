#!/usr/bin/python3
import requests
r = requests.get('https://intranet.hbtn.io/status')
print(type(r.text))
print(r.text)
