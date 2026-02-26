"""
Problem: Web 07 - HTTP: The HEAD Method

Category: Web Security

Description: Get only the headers of a get response

Algorith:
- Use the 'head' function for the call
- Show the data and get the flag

"""

import requests

response = requests.head("http://web-07.challs.olicyber.it/")

print(response.headers)