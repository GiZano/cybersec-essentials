"""
Problem: Crypto 04 - Xor 1

Category: Cryptography

Description: Get the flag by using xor between the numbers

Algorith:
- Define xor function 
- Transform given hexacodes into bytes
- Xor the two values
- Decode the flag
- Print the flag

"""

def xor(a, b):
    return bytes([x^y for x,y in zip(a,b)])

m1 = '158bbd7ca876c60530ee0e0bb2de20ef8af95bc60bdf'
m2 = '73e7dc1bd30ef6576f883e79edaa48dcd58e6aa82aa2'

val1 = bytes.fromhex(m1)
val2 = bytes.fromhex(m2)

res = xor(val1, val2)

flag = res.decode('utf-8')

print(flag)