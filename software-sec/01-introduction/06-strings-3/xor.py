"""
Problem: Software 06 - Strings 3

Category: Software Security

Description: Third iteration of the string obfuscation challenges. 
Builds upon previous static analysis techniques to reverse-engineer a more 
complex string hiding mechanism (e.g., dynamic key generation, multi-stage XOR, 
or custom encoding) using Ghidra and a Python solver.

Algorithm:
- Point 1: Load the binary in Ghidra and locate the string verification logic in the main function.
- Point 2: Analyze the pseudo-code to identify the new decoding algorithm.
- Point 3: Extract the necessary components (ciphertext, keys, or custom logic) from the memory sections (.rodata, .data).
- Point 4: Implement the reverse algorithm in Python to decrypt the hidden flag.

"""

# values from sw-06
key_hex = 'b230bddc107ae17b2c3be2ec9901'
key = bytes.fromhex(key_hex)

flag_hex = 'd45cdcbb6b1ed34a4a5ed2dfac7c'
flag = bytes.fromhex(flag_hex)

chars = [x ^ y for x,y in zip(flag, key)]

flag = ''

for char in chars:
    flag += chr(char)

print(flag)