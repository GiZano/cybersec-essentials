"""
Problem: Web 10 - HTTP: The OPTIONS Method

Category: Web Security

Description: Try uncommon method to find the flag!

Algorith:
- OPTIONS shows different methods that are allowed, but sometimes it lies
- Try uncommon ones (put and patch) to find the hidden flag
- Show the flag

"""

import requests

response = requests.patch("http://web-10.challs.olicyber.it/")

print(response.headers)

