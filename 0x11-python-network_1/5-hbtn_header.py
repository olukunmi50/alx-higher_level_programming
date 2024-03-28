#!/usr/bin/python3
""" Uses requests module to reply for header info"""
import requests
from sys import argv

if __name__ == "__main__":
    call = requests.get(argv[1])
    print(call.headers.get('X-Request-Id'))
