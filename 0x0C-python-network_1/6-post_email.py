#!/usr/bin/python3
"""sends request to URL and displays the X-Request-Id"""
from urllib import request


if __name__ == "__main__":
    import requests
    import sys
    email = {"email": sys.argv[2]}
    p = requests.post(sys.argv[1], email)
    print(p.text)
