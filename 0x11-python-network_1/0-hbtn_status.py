#!/usr/bin/python3

"""Script to fecth alx-intranet.hbtn"""
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    body_response = response.read()
    utf8_content = body_response.decode('utf-8')

print("Body response:")
print("\t- type:", type(body_response))
print("\t- content:", body_response)
print("\t- utf8 content:", utf8_content)

