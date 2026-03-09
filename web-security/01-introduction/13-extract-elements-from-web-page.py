"""
Problem: Web 13: Web Technologies: Extract Elements from Web Page

Category: Web Security

Description: Rebuild flag from fragments by finding all highlighted letters.

Algorith:
- Get web page with requests
- Initialize BeautifulSoup object
- Use find_all with correct tag
- Append each letter
- Print the whole flag

"""

import requests
from bs4 import BeautifulSoup

url = 'http://web-13.challs.olicyber.it/'

flag = ''

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

for letter in soup.find_all('span'):
    flag += letter.text

print(flag)