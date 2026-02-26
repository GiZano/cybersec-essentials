"""
Problem: Web 01 - HTTP: a Simple GET Request

Category: Web Security

Description: Use the requests library to get the flag inside an http endpoint

Algorith:
- Get response with requests.get
- Print by using .text value of response

"""

import requests

response = requests.get("http://web-01.challs.olicyber.it/")

print(response.text)