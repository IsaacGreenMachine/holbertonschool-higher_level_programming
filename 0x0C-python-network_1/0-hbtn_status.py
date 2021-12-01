#!/usr/bin/python3
import urllib.request
"""fetches a website"""
if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status/') as r:
        html = r.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
