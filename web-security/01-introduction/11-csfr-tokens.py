"""
Problem: Web 11 - CSRF Tokens

Category: Web Security

Description: Get the flag, splitted in four pieces, inside the /flag_piece endpoint, by specifying the index and the csrf token given in the previous index.
          First you have to login in the login endpoint with a POST with JSON Body request and use in the first piece endpoint the given csrf.

Algorith:
- Login with username and password with POST request
- Get first CSRF token
- Using the token and index, get the first piece and next CSRF.
- Repeat this last action for the number of pieces (4)
- Save every piece and show it

"""

import requests, json

s = requests.Session()

# Get First token and cookies with login

payload = {'username': 'admin', 'password': 'admin'}
headers = {'Content-Type': 'application/json'}
csfr_token = s.post("http://web-11.challs.olicyber.it/login", data=json.dumps(payload), headers=headers)
data = csfr_token.json()

flag = ''

for i in range(4):
    
    payload_get = {'index' : i, 'csrf': data['csrf']}
    
    csrf_token = s.get("http://web-11.challs.olicyber.it/flag_piece", params=payload_get)
    data = csrf_token.json()
    flag += data['flag_piece']

print(flag)