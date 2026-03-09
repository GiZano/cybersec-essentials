"""
Problem: Web 15 - Web Technologies: External Resources

Category: Web Security

Description: Find flag in external resource file

Algorith:
- Get page with requests
- Find script link with BeautifulSoup find_all
- Get the location in the src attribute
- Find the flag with a regex

"""

import requests
from bs4 import BeautifulSoup
import re
import urllib

url = 'http://web-15.challs.olicyber.it/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

for resource in soup.find_all('script'):
    src = resource.get('src')

    if src:
        resource_url = urllib.parse.urljoin(url, resource.get('src')) 

        if resource_url:
            resource_data = requests.get(resource_url) 

            flag = re.search("flag{.*}", resource_data.text)

            if flag:
                print(flag[0])