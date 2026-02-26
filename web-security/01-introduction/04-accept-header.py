"""
Problem: Web 04: HTTP: The 'Accept' header

Category: Web Security

Description: Get data in a different format (xml instead of json) by specifying the 'Accept' header

Algorith:
- Define 'Accept' header with 'application/xml'
- Receive get data
- Show data

"""

import requests

headers = {'Accept' : 'application/xml'}

response = requests.get("http://web-04.challs.olicyber.it/users", headers=headers)

print(response.text)