#!/usr/bin/python3
""" Uses requests module to get header info and display body of response """
import requests
from sys import argv

if __name__ == "__main__":
    call = requests.post(argv[1], data={'email': argv[2]})
    print(call.text)
