#!/usr/bin/python3
"""sends POST to URL and displays response"""
if __name__ == "__main__":
    import requests
    import sys
    email = sys.argv[2]
    data = {"email": email}
    p = requests.post(sys.argv[1], data)
    print(p.text)
