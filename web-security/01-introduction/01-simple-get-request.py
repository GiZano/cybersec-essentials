"""
Problem: Web 01 - HTTP: a simple GET requests

Category: Web Security

Description: Use the requests library to get the flag inside an http endpoint

Algorith:
- get response with requests.get
- print by using .text value of response

"""

import requests

response = requests.get("http://web-01.challs.olicyber.it/")

print(response.text)