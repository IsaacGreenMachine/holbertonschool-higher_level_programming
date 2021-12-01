#!/usr/bin/python3
"""takes URL, sends request to URL, displays value of X-Request-Id"""
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
