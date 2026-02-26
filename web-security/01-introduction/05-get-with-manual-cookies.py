"""
Problem: Web 05 - HTTP: Manual Cookies

Category: Web Security

Description: Get flag by sending the cookie 'password' with value 'admin'

Algorith:
- Create dict with cookies (password = 'admin')
- Receive GET data
- Show data

"""

import requests

cookies = dict(password='admin')

response = requests.get("http://web-05.challs.olicyber.it/flag", cookies=cookies)

print(response.text)