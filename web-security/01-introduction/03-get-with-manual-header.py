"""
Problem: Web 03 - HTTP: GET with manual header

Category: Web Security

Description: Get flag in the endpoint using a manual header 'X-Password' to specify the password "admin"

Algorith:
- Define dict with headers
- Receive GET data specifying the header
- Show the flag

"""

import requests

headers = {'X-Password' : 'admin'}

response = requests.get("http://web-03.challs.olicyber.it/flag", headers = headers)

print(response.text)