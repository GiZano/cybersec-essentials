"""
Problem: Web 16 - Web Technologies: Simple Spider

Category: Web Security
Description: Visit all pages of site using a spider to navigate through all anchors to find the flag


Algorith:
- Save urls to visit in list and visited urls in set
- If there are urls to visit, visit them and check for flags
- If the flag is found, print 
- Else, add new urls to list by checking if they are in the visited set first

"""

import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

base_url = 'http://web-16.challs.olicyber.it/'

def find_flag():
    visited = set()
    to_visit = [base_url]

    while to_visit:
        current_url = to_visit.pop()

        if current_url in visited:
            continue

        print(f"Exploring {current_url}")

        visited.add(current_url)

        response = requests.get(current_url)

        flag = re.search('flag{.*?\}', response.text)

        if flag:
            print(f"Flag in {current_url}")
            print(flag.group(0))
            return
        
        soup = BeautifulSoup(response.text, 'html.parser')

        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                new_url = urljoin(base_url, href)

                if new_url not in visited and new_url.startswith(base_url):
                    to_visit.append(new_url)

if __name__ == '__main__':
    find_flag()
            