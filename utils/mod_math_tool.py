"""
TOOL: Modular Arithmetic Toolkit

Category: Cryptography
Description: Interactive CLI tool to calculate the Extended Euclidean Algorithm (EGCD) 
and the Modular Multiplicative Inverse. These mathematical operations are the absolute 
foundation for solving RSA cryptography challenges.

Algorithm:
- Option 1 (EGCD): Computes the Greatest Common Divisor and Bézout's coefficients (x, y) recursively.
- Option 2 (Inverse): Computes the modular inverse using Python's built-in pow() function, 
  catching the ValueError gracefully if the numbers are not coprime.
"""

menu = """
=== MODULAR MATH TOOLKIT ===
1) EGCD (a, b) [ax + by = gcd(a,b)]
2) Inverse modular (a, m) [u = a^-1 (mod m)]
============================
"""

def egcd(a, b):
    # Base case: when the remainder is 0, we found the GCD
    if a == 0:
        return (b, 0, 1)
    else:
        # Recursive call to perform the backward substitution automatically
        gcd, x, y = egcd(b % a, a)
        return (gcd, y - (b // a) * x, x)

def inverse(a, m):
    # In Python 3.8+, pow() with a negative exponent calculates the modular inverse natively
    return pow(a, -1, m)

if __name__ == '__main__':

    while True:
        print(menu)
        
        try:
            selected = int(input('Select an option (Ctrl+C to exit): '))
        except ValueError:
            print("[!] Please enter a valid number.")
            continue
            
        match(selected):
            case 1:
                print("\n--- EGCD ---")
                a = int(input('Enter a: '))
                b = int(input('Enter b: '))
                gcd, x, y = egcd(a, b)
                print(f'\n[*] Equation is: {x}*({a}) + {y}*({b}) = {gcd}')
                print(f"[*] X is: {x}")
                print(f"[*] Y is: {y}\n")
                
            case 2:
                print("\n--- Modular Inverse ---")
                a = int(input('Enter base (a): '))
                m = int(input('Enter modulus (m): '))
                try:
                    inversed = inverse(a, m)
                    print(f'\n[*] The modular inverse is: {inversed}\n')
                except ValueError:
                    # This happens when GCD(a, m) != 1
                    print('\n[!] Error: Base is not invertible for the given modulus! (They are not coprime)\n')
            
            case _:
                print("\n[!] Invalid selection. Choose 1 or 2.")