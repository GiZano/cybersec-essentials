"""
Problem: Crypto 09 - Inverse Modular

Category: Cryptography

Description: Calculate inverse modulars and egcds

Algorith:
- Use custom made functions to solve problems about inverse modulars

"""

menu = """
1) EGCD (a, b) [ax + by = gcd(a,b)]
2) Inverse modular (a, m) [u = a^-1 (mod m)]
"""

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = egcd(b % a, a)
        return (gcd, y - (b // a) * x, x)

def inverse(a, m):
    return pow(a, -1, m)

if __name__ == '__main__':

    while True:
        print(menu)
        selected = int(input('Select: '))
        match(selected):
            case 1:
                a = int(input('a:'))
                b = int(input('b:'))
                gcd, x, y = egcd(a, b)
                print(f'Equation is: {x}*({a}) + {y}*({b}) = {gcd}')
                print(f"X is {x}")
                print(f"Y is {y}")
            case 2:
                a = int(input('a:'))
                m = int(input('m:'))
                try:
                    inversed = inverse(a, m)
                    print(inversed)
                except ValueError:
                    print('Base is not invertible for the given modulus!')