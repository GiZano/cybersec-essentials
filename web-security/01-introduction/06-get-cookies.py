"""
Problem: Web 06 - HTTP: Receive cookies

Category: Web Security

Description: Get cookies from a subdirectory and use them to get the flag.

Algorith:
- Initialize a session to store cookies
- Send a request to the /token resource to receive the cookies
- Send a request to the /flag resource to get the flag
- Show the flag

"""

import requests

session = requests.Session()

session.get("http://web-06.challs.olicyber.it/token")

response = session.get("http://web-06.challs.olicyber.it/flag")

print(response.text)