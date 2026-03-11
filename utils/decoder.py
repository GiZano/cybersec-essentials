"""
TOOL: Universal Decoder (Base64 / Hex / BigInt)

Category: Cryptography
Description: A collection of ready-to-use snippets and functions for fast 
conversions between strings, bytes, hexadecimal, Base64, and giant integers.

Algorithm:
- Base64 encoding/decoding using the standard 'base64' library.
- Hexadecimal conversions using built-in bytes.fromhex() and .hex().
- Big Integer to Bytes conversion using the exact bit_length() math trick.
"""

import base64

# ==========================================
# 1. BASE64 CONVERSIONS
# ==========================================

def b64_to_str(b64_string):
    """Decodes a Base64 string back to readable UTF-8 text."""
    decoded_bytes = base64.b64decode(b64_string)
    return decoded_bytes.decode('utf-8')

def str_to_b64(text):
    """Encodes a standard UTF-8 string into Base64."""
    text_bytes = text.encode('utf-8')
    b64_bytes = base64.b64encode(text_bytes)
    return b64_bytes.decode('utf-8')


# ==========================================
# 2. HEXADECIMAL CONVERSIONS
# ==========================================

def hex_to_str(hex_string):
    """Converts a Hexadecimal string to readable UTF-8 text."""
    # Removes '0x' prefix if present
    if hex_string.startswith('0x'):
        hex_string = hex_string[2:]
    decoded_bytes = bytes.fromhex(hex_string)
    return decoded_bytes.decode('utf-8')

def str_to_hex(text):
    """Encodes a standard UTF-8 string into Hexadecimal."""
    text_bytes = text.encode('utf-8')
    return text_bytes.hex()


# ==========================================
# 3. BIG INTEGER (BASE 10) CONVERSIONS
# ==========================================

def bigint_to_str(big_int):
    """
    Converts a giant mathematical integer (e.g., from RSA) back to text.
    Uses the bit_length() trick to dynamically calculate the exact bytes needed.
    """
    # Calculate the exact number of bytes required
    n_bytes = (big_int.bit_length() + 7) // 8
    
    # Convert to bytes (Big Endian) and decode
    decoded_bytes = big_int.to_bytes(n_bytes, 'big')
    return decoded_bytes.decode('utf-8')

def str_to_bigint(text):
    """Converts a text string into a single giant mathematical integer."""
    text_bytes = text.encode('utf-8')
    return int.from_bytes(text_bytes, 'big')


# ==========================================
# DEMO / TEST BLOCK
# ==========================================
if __name__ == '__main__':
    print("[*] Universal Decoder loaded.")
    
    # Quick test to ensure everything works
    flag = "flag{y0u_4r3_4_m4st3r_d3c0d3r}"
    
    print("\n--- Testing Conversions ---")
    print(f"Original: {flag}")
    
    b64_test = str_to_b64(flag)
    print(f"To Base64: {b64_test}")
    
    hex_test = str_to_hex(flag)
    print(f"To Hex:    {hex_test}")
    
    int_test = str_to_bigint(flag)
    print(f"To BigInt: {int_test}")
    
    print("\n--- Reversing Conversions ---")
    print(f"From Base64: {b64_to_str(b64_test)}")
    print(f"From Hex:    {hex_to_str(hex_test)}")
    print(f"From BigInt: {bigint_to_str(int_test)}")