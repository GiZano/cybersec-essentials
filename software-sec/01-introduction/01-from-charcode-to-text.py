"""
Problem: Crypto 01 - Encoding 1

Category: Cryptography

Description: Translate flag from charcode to text

Algorith:
- Translate each char and append it to the flag
- Print the flag

"""

chars = [102, 108, 97, 103, 123, 117, 103, 104, 95, 78, 117, 109, 66, 51, 114, 53, 95, 52, 49, 114, 51, 52, 100, 121, 125]

flag = "".join(chr(char) for char in chars)

print(flag)