"""
Problem: Crypto 01 - Encoding 2

Category: Cryptography

Description: Translate flag from hexacode to text

Algorith:
- Translate code using bytes lib
- Print the flag

"""

hexacode = '666c61677b68337834646563696d616c5f63346e5f62335f41424144424142457d'

flag = bytes.fromhex(hexacode).decode('utf-8')

print(flag)