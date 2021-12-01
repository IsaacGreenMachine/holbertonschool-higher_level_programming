#!/usr/bin/python3
"""sends request to URL and displays response with HTTPError handling"""
if __name__ == "__main__":
    from sys import argv
    import urllib.request
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except Exception as ex:
        print("Error code: {}".format(ex.code))
