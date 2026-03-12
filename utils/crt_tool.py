"""
TOOL: Chinese Remainder Theorem (CRT) Solver

Category: Cryptography
Description: Solves a system of modular congruences using the Chinese Remainder Theorem.
The condition for this to work is that all moduli must be pairwise coprime.

Algorithm:
- Calculates the total product of all moduli (M).
- For each equation, calculates the partial product (p = M / m_i).
- Computes the modular inverse of 'p' modulo 'm_i'.
- Sums all the partial results and applies modulo M to the final sum.
"""

from functools import reduce

def chinese_remainder_theorem(remainders, moduli):
    # 1. Calculate the total product of all moduli (M)
    prod_moduli = reduce(lambda a, b: a * b, moduli)
    
    sum_x = 0
    
    # 2. Apply the CRT formula for each equation
    for n_i, a_i in zip(moduli, remainders):
        # 'p' is the product of all moduli EXCEPT the current one
        p = prod_moduli // n_i
        
        # Find the modular inverse (using Python's native pow function)
        inv = pow(p, -1, n_i)
        
        # Add the partial result to the total sum
        sum_x += a_i * p * inv
        
    # 3. The final result is the total sum modulo M
    return sum_x % prod_moduli

if __name__ == '__main__':
    print("[*] Starting CRT Solver...")
    
    # TODO: UPDATE THESE LISTS WITH THE NUMBERS FROM THE SERVER
    # Format: x % modulus = remainder
    moduli =     [44, 65, 81, 61, 41]
    remainders = [32, 21, 75, 15, 21]
    
    result = chinese_remainder_theorem(remainders, moduli)
    
    print(f"\n[+] Your target x is: {result}")
    print(f"[*] Copy and paste this number into your netcat terminal!")