#!/usr/bin/python3
"""takes GitHub credentials (username and password)
   uses the GitHub API to display the id"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    usr = sys.argv[1]
    pswd = sys.argv[2]
    url = 'https://api.github.com/user'
    g = requests.get('https://api.github.com/user', auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    print(g.json().get('id'))
