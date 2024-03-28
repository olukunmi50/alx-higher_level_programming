#!/usr/bin/python3
""" Uses requests module. Prints api"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": argv[1][0] if len(argv) > 1 else ""}
    call = requests.post(url, data=data)
    try:
        b = call.json()
        if not b:
            print("No result")
        else:
            print("[{}] {}".format(b.get("id"), b.get("name")))
    except ValueError:
        print("Not a valid JSON")
