#!/usr/bin/python3
"""sends request to URL and displays the X-Request-Id"""
if __name__ == "__main__":
    import requests
    import sys
    r = requests.get(sys.argv[1])
    print(r.headers.get("X-Request-Id"))
