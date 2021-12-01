#!/usr/bin/python3
"""sends POST to URL and displays response"""
from urllib import request
if __name__ == "__main__":
    import requests
    import sys
    email = {"email": sys.argv[2]}
    p = requests.post(sys.argv[1], email)
    print(p.text)
