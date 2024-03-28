#!/usr/bin/python3
""" Sends a POST request to the passed URL with the email """

if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

 data = parse.urlencode({"email": sys.argv[2]}).encode()
    with request.urlopen(sys.argv[1], data) as response:
        print(response.read().decode('utf-8'))
