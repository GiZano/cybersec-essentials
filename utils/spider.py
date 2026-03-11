"""
TOOL: Simple Web Spider

Problem: Web Technologies - Simple Spider
Category: Web Security

Description: Visit all pages of a site using a spider to navigate through all anchors to find the flag.
Optimized with requests.Session() for maximum speed during CTFs.

Algorithm:
- Save urls to visit in a list (DFS stack) and visited urls in a set
- Reuse TCP connections with Session
- Extract all valid hrefs and append to stack if not visited and within scope
- Stop and print when regex matches the flag
"""

import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

# TODO: Put URL here before launching
base_url = 'http://web-16.challs.olicyber.it/'

def find_flag():
    visited = set()
    to_visit = [base_url]
    
    # Usiamo una Sessione per velocizzare le richieste HTTP (Keep-Alive)
    session = requests.Session()
    
    # Regex compilata per la flag (con la 'r' per la Raw String)
    flag_pattern = re.compile(r'flag\{.*?\}')

    while to_visit:
        current_url = to_visit.pop()

        if current_url in visited:
            continue

        print(f"[*] Exploring {current_url}")
        visited.add(current_url)

        try:
            response = session.get(current_url, timeout=3)
        except requests.RequestException as e:
            print(f"[!] Error on {current_url}: {e}")
            continue

        # Cerchiamo la flag
        flag = flag_pattern.search(response.text)
        if flag:
            print(f"\n🎉 FLAG FOUND in {current_url}")
            print(f"🚩 {flag.group(0)}")
            return
        
        # Facciamo il parsing dei link
        soup = BeautifulSoup(response.text, 'html.parser')

        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                new_url = urljoin(base_url, href)
                # Togliamo eventuali ancore interne (es. #section1) che punterebbero alla stessa pagina
                new_url = new_url.split('#')[0]

                if new_url not in visited and new_url.startswith(base_url):
                    to_visit.append(new_url)

if __name__ == '__main__':
    find_flag()