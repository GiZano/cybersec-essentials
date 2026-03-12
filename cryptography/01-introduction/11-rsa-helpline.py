"""
Problem: Crypto 11 - RSA Helpline

Category: Cryptography
Description: Encrypt a message and generate private/public keys using the RSA algorithm.

Algorithm:
- Define two prime numbers (p, q) and calculate the modulus (n = p * q).
- Calculate Euler's totient function, phi(n) = (p-1) * (q-1).
- Choose a public exponent (e) that is coprime with phi.
- Encrypt the message (m) using the public key: c = m^e mod n.
- Calculate the private key (d) as the modular inverse of e modulo phi.
- Decrypt the ciphertext (c) using the private key: m = c^d mod n.
"""

m = 17

p = 11
q = 13

# 1. Modulus
n = p * q

# 2. Euler's Totient
phi = (p - 1) * (q - 1)

# 3. Public Exponent
e = 19

# 4. Encrypt --> c = m^e mod n
c = pow(m, e, n)

# 5. Private key --> d = e^-1 mod phi (Crucial: modulo phi, NOT n!)
d = pow(e, -1, phi)

# 6. Decrypt --> m = c^d mod n
decrypted = pow(c, d, n)

# Print values with clean mathematical notation
print(f"[*] n:   {n} ( {p} * {q} )")
print(f"[*] phi: {phi} ( ({p}-1) * ({q}-1) )")
print(f"[*] c:   {c} ( {m}^{e} mod {n} )")
print(f"[*] d:   {d} ( {e}^-1 mod {phi} )")
print(f"\n[+] Decrypted: {decrypted} (Original: {m})")