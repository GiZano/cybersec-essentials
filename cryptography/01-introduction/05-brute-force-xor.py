"""
Problem: Crypto 05 - Xor 2

Category: Cryptography

Description: Get the flag by brute forcing one byte long xor

Algorith:
- Translate the text into bytes
- Get all possible numbers that appear in a byte (2^8 -> 256)
- Xor using the generated numbers and the ciphertext
- Decode the result
- Print the flag
- Find the flag that makes sense

"""

def xor(a, b):
    return bytes([x^y for x,y in zip(a,b)])

ciphertext = '104e137f425954137f74107f525511457f5468134d7f146c4c'

bytes_ciphertext = bytes.fromhex(ciphertext)

for x in range(256):
    res = bytes([b ^ x for b in bytes_ciphertext])

    try:
        decoded = res.decode('utf-8')

        print(f"Chiave {x} (Hex: {hex(x)}): flag{{{decoded}}}")
    except UnicodeDecodeError:
        pass