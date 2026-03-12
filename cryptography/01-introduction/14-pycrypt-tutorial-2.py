"""
Problem: Crypto 14 - Pycryptutorial 2

Category: Cryptography

Description: Solves an interactive PyCryptodome tutorial challenge by implementing 
various cryptographic primitives. It covers hashing (SHA3 family), message authentication 
(HMAC), parsing asymmetric keys (DSA), and number theory utilities (prime generation 
and primality testing).

Algorithm:
- Calculate the SHA3-384 hash of a given byte string.
- Compute the HMAC-SHA224 of a message using a decoded hexadecimal secret key.
- Import a hex-encoded DSA private key and extract its mathematical components (g, p, x, y).
- Generate a cryptographically secure random prime number of a specific bit length (1347 bits).
- Verify the primality of a given large integer using PyCryptodome's built-in primality tester.

"""

# 1. Normal Hash
from Crypto.Hash import SHA3_384

msg = b'hash_me_pls'

h = SHA3_384.new()
h.update(msg)
print(h.hexdigest())

###
print()
# 2. HMAC Hash
from Crypto.Hash import HMAC, SHA224

key_hex = '25b7332cd016fe770200633c59d4e56a3499255119c4367545dde4336d35c68b'
secret = bytes.fromhex(key_hex)
msg = 'La mia integrità è importante!'.encode('utf-8')

h = HMAC.new(secret, digestmod=SHA224)
h.update(msg)

print(h.hexdigest())

### 
print()
# 3. DSA Hash
from Crypto.PublicKey import DSA

key_hex = '3082025b0201003082023506072a8648ce380401308202280282010100ae158c6526c93967bdca9fc7b8e366231c637acd0619e1a0a91509f5e2df7fba2daea73303c7e552ccadc34b6587e07285fe6e8c031c0a41c1e997ed63199cc3e45a66e46e1aa14452bb17c7d4d0201f536fc459d5a6ad5275796ff7aa243aae6a500977ed0bbdd5bd9d8c427f7a9e01a822caca99f373018dfc35f40a153642983d1223b6aec4682abfde7226e6865d9282fb599742d6bcd5eb9ee08492378d9c78c0d29562caea76d1470b933a30dc4e92f160bc367be8febbde61394a9fb46483b448fc3a571855c99199a5525c2244708efa0896a3487e7c7af75528b9bdc4cfad5c03f7b2db27cc184ba623369474259a95edbb36d7e151a63cca7ca971021d0089b53ebd02e740f0d581a815e5e83d15d6c97c9bc9414e2cf63f55fb0282010076c3916b319a1a79f80d1766448069fee3bdda81340fb3a5e787742df295bfd516824382e2c4cf186c1d2cb8c627535197621ed9d7940eb324f06a54c83dd179e8cdd1cc69786d3a1768b95be14aaa4cb6b784fa603c3a96b49669f5e1dc0bc9c5db9634e104ae750ccea57a7580f9d95d34f60af2cf07979559505df376d9fefc2e394ada1be8a5841d91c61953976c64463bea0933f9ac0d8f1fc6295a0f807db306da1f506230333e70a0104660c5a36e76c75b91a02c33b09afeeb8bcbda681870fb2a292d09e84f368104bce786f0f8a4109e4dcaf31c743b254ec5d744e018cef2fa6a939b7f4f984381941b434b70d35744a1f40f9ce701ac003d3e74041d021b6bc69ab4dd1c991c7cd3445d95234620a618d88161b71bdc10ebb6'

secret = bytes.fromhex(key_hex)

dsakey = DSA.import_key(secret)

print(f"g: {dsakey.domain()[2]}")
print(f"p: {dsakey.domain()[0]}")
print(f"x: {dsakey.x}")
print(f"y: {dsakey.y}")

###
print()
# 4. Primary Number of x bits
from Crypto.Util.number import getPrime

prime = getPrime(1347)
print(f"1347 bits prime: {prime}")

###
print()
# 5. x is prime?
from Crypto.Util.number import isPrime

p = 112447235816417132566301619799732849902468285913058960319074074443670038376777503880136849645859987185910512799384817786946123409334094815099233690768484225570670935714074420634451416596557518915611106433036046958040039183489587124990900370463791634729020509473519278914591148800382529074179139361573666388543

print(f"{p} is prime? {isPrime(p)}")