#!/usr/bin/python3
""" Fetches header from url & display body of response """

from urllib import request, parse, error
import sys

if __name__ == "__main__":

 argv = sys.argv
    url = argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.status))
