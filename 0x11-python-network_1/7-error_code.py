#!/usr/bin/python3
""" Prints error code """
import requests
from sys import argv

if __name__ == "__main__":
    call = requests.get(argv[1])
    if call.status_code > 400:
        print("Error code:", call.status_code)
    else:
        print(call.text)
