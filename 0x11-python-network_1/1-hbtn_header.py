#!/usr/bin/python3
""" Fetches header from url """

if __name__ == "__main__":
    import sys
    import urllib.request
  with request.urlopen(sys.argv[1]) as response:
        print(response.getheader("X-Request-Id"))
