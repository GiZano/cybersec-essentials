"""
TOOL: Number Theory & Modular Math Toolkit

Category: Cryptography
Description: A unified library and interactive CLI for essential number theory 
operations: EGCD, Modular Inverse, Chinese Remainder Theorem (CRT), and 
Discrete Logarithm Problem (DLP) Bruteforcing.
"""

from functools import reduce

# ==========================================
# 1. CORE MATH LIBRARIES (Importable)
# ==========================================

def egcd(a, b):
    """Extended Euclidean Algorithm."""
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = egcd(b % a, a)
        return (gcd, y - (b // a) * x, x)

def inverse(a, m):
    """Calculates the modular multiplicative inverse."""
    return pow(a, -1, m)

def crt(remainders, moduli):
    """Solves a system of congruences using the Chinese Remainder Theorem."""
    prod_moduli = reduce(lambda a, b: a * b, moduli)
    sum_x = 0
    
    for n_i, a_i in zip(moduli, remainders):
        p = prod_moduli // n_i
        # Guarda come riutilizziamo elegantemente la nostra funzione inverse!
        inv = inverse(p, n_i) 
        sum_x += a_i * p * inv
        
    return sum_x % prod_moduli

def dlp_bruteforce(g, h, p):
    """Bruteforces small Discrete Logarithms (g^x = h mod p)."""
    for x in range(1, p):
        if pow(g, x, p) == h:
            return x
    return None


# ==========================================
# 2. INTERACTIVE CLI MENU
# ==========================================

menu = """
=== NUMBER THEORY TOOLKIT ===
1) EGCD (Extended Euclidean Algorithm)
2) Modular Inverse
3) CRT (Chinese Remainder Theorem)
4) DLP Bruteforcer (Discrete Logarithm)
=============================
"""

if __name__ == '__main__':
    while True:
        print(menu)
        
        try:
            selected = int(input('Select an option (Ctrl+C to exit): '))
        except ValueError:
            print("[!] Please enter a valid number.")
            continue
        except KeyboardInterrupt:
            print("\n\n[*] Exiting Number Theory Toolkit. Goodbye!")
            break
            
        match(selected):
            case 1:
                print("\n--- EGCD ---")
                try:
                    a = int(input('Enter a: '))
                    b = int(input('Enter b: '))
                    gcd, x, y = egcd(a, b)
                    print(f'\n[*] Equation is: {x}*({a}) + {y}*({b}) = {gcd}')
                    print(f"[*] X is: {x}")
                    print(f"[*] Y is: {y}\n")
                except ValueError:
                    print("[!] Error: Invalid input.")

            case 2:
                print("\n--- Modular Inverse ---")
                try:
                    a = int(input('Enter base (a): '))
                    m = int(input('Enter modulus (m): '))
                    inversed = inverse(a, m)
                    print(f'\n[*] The modular inverse is: {inversed}\n')
                except ValueError as e:
                    if "invertible" in str(e) or "base is not invertible" in str(e):
                        print('\n[!] Error: Base is not invertible for the given modulus! (Not coprime)\n')
                    else:
                        print("[!] Error: Invalid input.")

            case 3:
                print("\n--- Chinese Remainder Theorem ---")
                print("[*] Note: Enter values separated by spaces (e.g., '44 65 81')")
                try:
                    mods_input = input('Enter moduli (m_i): ')
                    rems_input = input('Enter remainders (a_i): ')
                    
                    moduli = [int(x) for x in mods_input.split()]
                    remainders = [int(x) for x in rems_input.split()]
                    
                    if len(moduli) != len(remainders):
                        print("[!] Error: You must provide the same number of moduli and remainders.\n")
                        continue
                        
                    result = crt(remainders, moduli)
                    print(f"\n[+] CRT Result (x): {result}\n")
                except Exception as e:
                    print(f"[!] Error processing lists: {e}\n")

            case 4:
                print("\n--- DLP Bruteforcer ---")
                print("[*] Equation: g^x = h (mod p)")
                try:
                    g = int(input('Enter base (g): '))
                    h = int(input('Enter result (h): '))
                    p = int(input('Enter prime modulus (p): '))
                    
                    print("[*] Bruteforcing... please wait.")
                    res = dlp_bruteforce(g, h, p)
                    if res:
                        print(f"\n[+] Found! x = {res}\n")
                    else:
                        print("\n[!] No solution found within the given modulus.\n")
                except ValueError:
                    print("[!] Error: Invalid input.")

            case _:
                print("\n[!] Invalid selection. Please choose a valid option.\n")