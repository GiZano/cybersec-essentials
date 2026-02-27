"""
Problem: Web 09 - HTTP: A POST Request with JSON Body

Category: Web Security

Description: Get the flag by sending a POST in which we specify a form data, formatting in json format

Algorith:
- Prepare payload with key-value pairs (username and password)
- Prepare headers specyfing content type is json
- Send POST request containin the payload in his body (set the data attribute and dump with json library) and set headers
- Show data

"""

import requests, json

payload = {'username': 'admin', 'password': 'admin'}
headers = {'Content-Type': 'application/json'}

response = requests.post("http://web-09.challs.olicyber.it/login", data=json.dumps(payload), headers=headers)

print(response.text)