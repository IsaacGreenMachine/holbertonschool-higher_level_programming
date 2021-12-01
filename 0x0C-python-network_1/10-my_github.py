#!/usr/bin/python3
"""takes github credentials and displays ID"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    g = requests.get('https://api.github.com/user',
                     auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    print(g.json().get('id'))
