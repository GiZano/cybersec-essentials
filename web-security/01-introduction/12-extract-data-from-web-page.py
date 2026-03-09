"""
Problem: Web 12 - Web Technologies: Extract Simple Content from Web Page

Category: Web Security

Description: Use Beautiful Soup to extract paragraphs from web page and find the flag.

Algorith:
- Get page with requests get
- Get soup object
- Use find_all function to find all paragraphs
- Print paragraphs which contains the flag

"""

import requests
from bs4 import BeautifulSoup


url = 'http://web-12.challs.olicyber.it/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

for string in soup.find_all('p'):
    if 'flag' in string.text:
        print(string.text)
