#!/usr/bin/python3
"""sends request to URL and displays the X-Request-Id"""
if __name__ == "__main__":
    import requests
    import sys
    if len(sys.argv) < 2 or sys.argv[1] == None:
        data = {"q": ""}
    else:
        data = {"q": sys.argv[1]}
    p = requests.post('http://0.0.0.0:5000/search_user', data=data)
    if p.json() == {}:
        print("No result")
    else: 
        jid = p.json().get("id")
        name = p.json().get("name")
        print("[{}] {}".format(jid, name))
