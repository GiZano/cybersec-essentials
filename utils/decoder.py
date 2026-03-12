"""
TOOL: Universal Decoder (Base64 / Hex / BigInt)

Category: Cryptography
Description: A CLI toolkit and library for fast conversions between 
strings, bytes, hexadecimal, Base64, and giant integers.

Algorithm:
- Base64 encoding/decoding using the standard 'base64' library.
- Hexadecimal conversions using built-in bytes.fromhex() and .hex().
- Big Integer to Bytes conversion using the exact bit_length() math trick.
- Hexadecimal to Big Integer using native base 16 conversion.
"""

import base64

# ==========================================
# 1. BASE64 CONVERSIONS
# ==========================================
def b64_to_str(b64_string):
    decoded_bytes = base64.b64decode(b64_string)
    return decoded_bytes.decode('utf-8')

def str_to_b64(text):
    text_bytes = text.encode('utf-8')
    b64_bytes = base64.b64encode(text_bytes)
    return b64_bytes.decode('utf-8')

# ==========================================
# 2. HEXADECIMAL CONVERSIONS (TEXT)
# ==========================================
def hex_to_str(hex_string):
    if hex_string.startswith('0x'):
        hex_string = hex_string[2:]
    decoded_bytes = bytes.fromhex(hex_string)
    return decoded_bytes.decode('utf-8')

def str_to_hex(text):
    text_bytes = text.encode('utf-8')
    return text_bytes.hex()

# ==========================================
# 3. BIG INTEGER (BASE 10) CONVERSIONS
# ==========================================
def bigint_to_str(big_int):
    n_bytes = (big_int.bit_length() + 7) // 8
    decoded_bytes = big_int.to_bytes(n_bytes, 'big')
    return decoded_bytes.decode('utf-8')

def str_to_bigint(text):
    text_bytes = text.encode('utf-8')
    return int.from_bytes(text_bytes, 'big')

# ==========================================
# 4. HEX <--> BIG INTEGER CONVERSIONS
# ==========================================
def hex_to_bigint(hex_string):
    """Converts a Hexadecimal string directly to a math Big Integer."""
    if hex_string.startswith('0x'):
        hex_string = hex_string[2:]
    return int(hex_string, 16)

def bigint_to_hex(big_int):
    """Converts a math Big Integer directly to a Hexadecimal string."""
    return hex(big_int)[2:]


# ==========================================
# INTERACTIVE CLI MENU
# ==========================================
menu = """
=== UNIVERSAL DECODER CLI ===
1) Encode: String -> Base64
2) Decode: Base64 -> String
3) Encode: String -> Hexadecimal
4) Decode: Hexadecimal -> String
5) Encode: String -> Big Integer
6) Decode: Big Integer -> String
7) Decode: Hexadecimal -> Big Integer (For Math)
8) Encode: Big Integer -> Hexadecimal
=============================
"""

if __name__ == '__main__':
    while True:
        print(menu)
        
        try:
            selected = int(input('Select an option (Ctrl+C to exit): '))
        except ValueError:
            print("[!] Please enter a valid number.\n")
            continue
        except KeyboardInterrupt:
            print("\n\n[*] Exiting Universal Decoder. Goodbye!")
            break
            
        match(selected):
            case 1:
                print("\n--- String to Base64 ---")
                txt = input("Enter string: ")
                print(f"[+] Result: {str_to_b64(txt)}\n")
            case 2:
                print("\n--- Base64 to String ---")
                b64 = input("Enter Base64: ")
                try:
                    print(f"[+] Result: {b64_to_str(b64)}\n")
                except Exception as e:
                    print(f"[!] Error: {e}\n")
            case 3:
                print("\n--- String to Hexadecimal ---")
                txt = input("Enter string: ")
                print(f"[+] Result: {str_to_hex(txt)}\n")
            case 4:
                print("\n--- Hexadecimal to String ---")
                h = input("Enter Hexadecimal: ").strip()
                try:
                    print(f"[+] Result: {hex_to_str(h)}\n")
                except Exception as e:
                    print(f"[!] Error: {e}\n")
            case 5:
                print("\n--- String to Big Integer ---")
                txt = input("Enter string: ")
                print(f"[+] Result: {str_to_bigint(txt)}\n")
            case 6:
                print("\n--- Big Integer to String ---")
                try:
                    bi = int(input("Enter Big Integer: "))
                    print(f"[+] Result: {bigint_to_str(bi)}\n")
                except Exception as e:
                    print(f"[!] Error: {e}\n")
            case 7:
                print("\n--- Hexadecimal to Big Integer ---")
                h = input("Enter Hexadecimal: ").strip()
                try:
                    print(f"[+] Result: {hex_to_bigint(h)}\n")
                except Exception as e:
                    print(f"[!] Error: Make sure it is valid Hex. {e}\n")
            case 8:
                print("\n--- Big Integer to Hexadecimal ---")
                try:
                    bi = int(input("Enter Big Integer: "))
                    print(f"[+] Result: {bigint_to_hex(bi)}\n")
                except Exception as e:
                    print(f"[!] Error: {e}\n")
            case _:
                print("\n[!] Invalid selection.\n")