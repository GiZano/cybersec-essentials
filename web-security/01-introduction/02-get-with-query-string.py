"""
Problem: Web 02 - HTTP: GET request with query string

Category: Web Security

Description: Get flag from http endpoint by specifying the attribute "id" as "flag"

Algorith:
- define payload (id = 'flag')
- get http response
- show flag with .text

"""

import requests

payload = {'id' : 'flag'}

response = requests.get("http://web-02.challs.olicyber.it/server-records", params = payload)

print(response.text)