#!/usr/bin/python3
""" Scripts that fetches url """
import requests

if __name__ == "__main__":
call =  requests.get('https://alx-intranet.hbtn.io/status')
 print("Body response:\n\t- type: {}\n\t- content: {}"
          .format(type(call.text), call.text))
