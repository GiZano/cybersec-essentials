"""
Problem: Crypto 03 - Encoding 3

Category: Cryptography

Description: Translate flag from base64 and base10

Algorith:
- Traslate the b64 part using the b64decode function from the base64 lib
- Calculate the needed n_bytes
- Transform the b10 code in bytes and decode into text
- Print the flag

"""

from base64 import b64decode

b64_code = 'ZmxhZ3t3NDF0XzF0c19hbGxfYjE='

b10_code = 664813035583918006462745898431981286737635929725

flag = b64decode(b64_code).decode('utf-8')

n_bytes = (b10_code.bit_length() + 7) // 8

flag += b10_code.to_bytes(n_bytes, 'big').decode('utf-8')

print(flag)