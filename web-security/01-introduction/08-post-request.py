"""
Problem: Web 08 - HTTP: A Traditional POST Request

Category: Web Security

Description: Get the flag by sending a POST in which we specify a form data

Algorith:
- Prepare payload with key-value pairs (username and password)
- Send POST request containin the payload in his body (set the data attribute)
- Show data

"""

import requests

payload = {'username': 'admin', 'password': 'admin'}

response = requests.post("http://web-08.challs.olicyber.it/login", data=payload)

print(response.text)