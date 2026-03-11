"""
TOOL: Single-Byte XOR Brute-Forcer

Category: Cryptography
Description: Get the flag by brute-forcing a single-byte XOR key.
Automatically filters out non-printable garbage text using UTF-8 decoding logic.

Algorithm:
- Translate the hex ciphertext into bytes.
- Loop through all possible 256 byte values (0-255).
- XOR every byte of the ciphertext with the current key.
- Decode the result using UTF-8.
- Ignore UnicodeDecodeErrors and print only readable outputs.
"""

def brute_force_single_byte_xor(ciphertext_hex):
    print(f"[*] Starting Single-Byte XOR Brute-Force on: {ciphertext_hex[:15]}...")
    
    # Translate the hex string into raw bytes
    bytes_ciphertext = bytes.fromhex(ciphertext_hex)

    # Brute-force all 256 possible byte values
    for x in range(256):
        # XOR each byte 'b' of the ciphertext with our candidate key 'x'
        res = bytes([b ^ x for b in bytes_ciphertext])

        try:
            # Try to decode. If it contains invalid characters, it will throw an error
            decoded = res.decode('utf-8')
            
            # Formatting the output nicely with fixed widths for readability
            print(f"[+] Key {x:3} (Hex: {hex(x):>4}): flag{{{decoded}}}")
        except UnicodeDecodeError:
            # Silently ignore garbage outputs
            pass
            
    print("[*] Brute-force complete!\n")

if __name__ == '__main__':
    # TODO: Paste your target ciphertext here before running
    TARGET_CIPHERTEXT = '104e137f425954137f74107f525511457f5468134d7f146c4c'
    brute_force_single_byte_xor(TARGET_CIPHERTEXT)