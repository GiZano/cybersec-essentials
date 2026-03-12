"""
TOOL: Diffie-Hellman Ultimate Toolkit

Category: Cryptography
Description: An interactive CLI toolkit containing all the essential
utilities to solve Diffie-Hellman Key Exchange challenges, including
hybrid AES-CBC decryption using the derived shared secret.

Features:
- Simulate Client-side DH Exchange (All-in-one)
- Generate standardized 1024-bit Safe Primes
- Find valid generators (primitive roots) for Safe Primes
- Decrypt AES-CBC messages using the DH Shared Secret
- Generate DH Keypair (Independent generation)
- Calculate Shared Secret (Independent calculation)
"""

import random
import hashlib
try:
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import unpad
    from Crypto.Util.number import long_to_bytes
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False

menu = """
=== DIFFIE-HELLMAN TOOLKIT ===
1) Simulate DH Key Exchange (All-in-one)
2) Generate 1024-bit Safe Prime (RFC 2409)
3) Find Valid Generator for a Safe Prime
4) Decrypt AES-CBC with Shared Secret (Hybrid Crypto)
--- ASYNC DH EXCHANGE ---
5) Generate My Keypair (Calculate b and B)
6) Calculate Shared Secret (Calculate S)
==============================
"""

def diffie_hellman_exchange(p, g, server_public_key):
    b = random.randint(2, p - 2)
    my_public_key = pow(g, b, p)
    shared_secret = pow(server_public_key, b, p)
    return b, my_public_key, shared_secret

def generate_dh_keypair(p, g):
    b = random.randint(2, p - 2)
    B = pow(g, b, p)
    return b, B

def calculate_shared_secret(p, b, A):
    return pow(A, b, p)

def get_rfc2409_safe_prime():
    hex_p = (
        "FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD1"
        "29024E088A67CC74020BBEA63B139B22514A08798E3404DD"
        "EF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245"
        "E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7ED"
        "EE386BFB5A899FA5AE9F24117C4B1FE649286651ECE65381"
        "FFFFFFFFFFFFFFFF"
    )
    return int(hex_p, 16)

def find_primitive_root(p):
    q = (p - 1) // 2
    for g in range(2, 1000):
        if pow(g, 2, p) != 1 and pow(g, q, p) != 1:
            return g
    return None

def decrypt_aes_with_dh_secret(shared_secret_int, iv_hex, msg_hex):
    iv = bytes.fromhex(iv_hex)
    msg = bytes.fromhex(msg_hex)
    
    candidates = []
    
    try:
        candidates.append(("Padded 128-byte", shared_secret_int.to_bytes(128, 'big')))
    except Exception:
        pass
        
    candidates.append(("Unpadded long_to_bytes", long_to_bytes(shared_secret_int)))
    
    candidates.append(("String encoded", str(shared_secret_int).encode()))
    
    candidates.append(("Hex encoded", hex(shared_secret_int)[2:].encode()))

    for desc, sec_bytes in candidates:
        
        for kl in [16, 24, 32]:
            if len(sec_bytes) >= kl:
                aes_key = sec_bytes[:kl]
                try:
                    cipher = AES.new(aes_key, AES.MODE_CBC, iv)
                    decrypted = unpad(cipher.decrypt(msg), AES.block_size)
                    return f"Direct {kl}-bytes ({desc})", decrypted.decode('utf-8', errors='ignore')
                except ValueError:
                    pass
                    
        for algo_name, algo in [('MD5', hashlib.md5), ('SHA1', hashlib.sha1), ('SHA256', hashlib.sha256)]:
            hash_bytes = algo(sec_bytes).digest()
            for kl in [16, 24, 32]:
                if len(hash_bytes) >= kl:
                    aes_key = hash_bytes[:kl]
                    try:
                        cipher = AES.new(aes_key, AES.MODE_CBC, iv)
                        decrypted = unpad(cipher.decrypt(msg), AES.block_size)
                        return f"Hash {algo_name}[:{kl}] ({desc})", decrypted.decode('utf-8', errors='ignore')
                    except ValueError:
                        pass
                        
    return None, None

if __name__ == '__main__':
    while True:
        print(menu)
        
        try:
            selected = int(input('Select an option (Ctrl+C to exit): '))
        except ValueError:
            print("[!] Please enter a valid number.")
            continue
        except KeyboardInterrupt:
            print("\n\n[*] Exiting Diffie-Hellman Toolkit. Goodbye!")
            break
            
        match(selected):
            case 1:
                print("\n--- DH Simulator (All-in-one) ---")
                try:
                    p = int(input('Enter prime (p): '))
                    g = int(input('Enter generator (g): '))
                    server_pub = int(input("Enter Server's Public Key (A): "))
                    
                    b, B, S = diffie_hellman_exchange(p, g, server_pub)
                    
                    print(f"\n[*] Public Parameters: p={p}, g={g}")
                    print(f"[*] Server's Public Key (A): {server_pub}")
                    print(f"[-] My Generated Private Key (b): {b} (Secret!)")
                    
                    print(f"\n[+] YOUR PUBLIC KEY (B): {B}")
                    print(f"[+] SHARED SECRET (S): {S}\n")
                except ValueError:
                    print("[!] Error: Please enter valid integers.\n")
                    
            case 2:
                print("\n--- Safe Prime Generator ---")
                p = get_rfc2409_safe_prime()
                print("\n[+] 1024-bit Safe Prime (RFC 2409):")
                print(f"{p}\n")
                
            case 3:
                print("\n--- Generator Finder ---")
                try:
                    p = int(input('Enter Safe Prime (p): '))
                    print(f"[*] Calculating the sub-module q and searching...")
                    valid_g = find_primitive_root(p)
                    
                    if valid_g:
                        print(f"\n[+] Mathematically perfect generator found! g = {valid_g}\n")
                    else:
                        print("\n[!] No generator found in the first 1000 numbers.\n")
                except ValueError:
                    print("[!] Error: Please enter a valid integer.\n")

            case 4:
                print("\n--- AES-CBC DH Decryptor ---")
                if not CRYPTO_AVAILABLE:
                    print("[!] Error: 'pycryptodome' library is not installed.")
                    print("[*] Fix it by running: pip install pycryptodome\n")
                    continue
                
                try:
                    S = int(input("Enter Shared Secret (S) as integer: "))
                    iv_hex = input("Enter IV (hex): ").strip()
                    msg_hex = input("Enter Ciphertext Message (hex): ").strip()
                    
                    print("\n[*] Attempting decryption...")
                    key_len, plaintext = decrypt_aes_with_dh_secret(S, iv_hex, msg_hex)
                    
                    if plaintext:
                        print(f"[+] Success! Decrypted using AES-{key_len*8}.")
                        print(f"[+] FLAG: {plaintext}\n")
                    else:
                        print("[!] Decryption failed. Check your Shared Secret, IV, and Ciphertext.\n")
                except ValueError as e:
                    print(f"[!] Error: Invalid input format. {e}\n")

            case 5:
                print("\n--- Generate My Keypair ---")
                try:
                    p = int(input('Enter prime (p): '))
                    g = int(input('Enter generator (g): '))
                    
                    b, B = generate_dh_keypair(p, g)
                    
                    print(f"\n[-] My Generated Private Key (b): {b} (Keep this secret!)")
                    print(f"[+] YOUR PUBLIC KEY (B): {B} (Send this to Alice!)\n")
                except ValueError:
                    print("[!] Error: Please enter valid integers.\n")

            case 6:
                print("\n--- Calculate Shared Secret ---")
                try:
                    p = int(input('Enter prime (p): '))
                    b = int(input('Enter your Private Key (b): '))
                    A = int(input("Enter Server's Public Key (A): "))
                    
                    S = calculate_shared_secret(p, b, A)
                    
                    print(f"\n[+] SHARED SECRET (S): {S}\n")
                except ValueError:
                    print("[!] Error: Please enter valid integers.\n")
                    
            case _:
                print("\n[!] Invalid selection. Choose between 1 and 6.\n")