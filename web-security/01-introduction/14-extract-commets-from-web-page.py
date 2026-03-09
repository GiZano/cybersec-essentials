"""
Problem: Web 14 - Web Technologies: Extract Comments from Web Pages

Category: Web Security

Description: Get flag from comment in html file.

Algorith:
- Get page with requests
- Initialize BeautifulSoup object
- Use find_all with special comment object class
- Print flag

"""

import requests
import bs4
from bs4 import BeautifulSoup

url = 'http://web-14.challs.olicyber.it/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

for string in soup.find_all(string=bs4.element.Comment):
    if 'flag' in string:
        print(string)