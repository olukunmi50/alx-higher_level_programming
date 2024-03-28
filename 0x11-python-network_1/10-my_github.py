#!/usr/bin/python3
""" Uses requests module. Takes your github credentials """
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/user"
    auth = (argv[1], argv[2])
    call = requests.get(url, auth=auth)
    try:
        print(call.json().get("id"))
    except ValueError:
        print("Not a valid JSON")
