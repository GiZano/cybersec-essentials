from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

# Part 1

key_hex = 'c622e3493f26f79c'
key = bytes.fromhex(key_hex)

cipher = DES.new(key, DES.MODE_CBC)

data = 'La lunghezza di questa frase non è divisibile per 8'.encode('utf-8')

ct_bytes = cipher.encrypt(pad(data, DES.block_size, style='x923'))

print(f"Ciphertext: {ct_bytes.hex()}")
print(f"IV: {cipher.iv.hex()}")

# Part 1 end
print('\n-------\n')
# Part 2

from Crypto.Cipher import AES

key_hex = '00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff'
data = 'Mi chiedo cosa significhi il numero nel nome di questo algoritmo.'.encode('utf-8')
segment_size = 24

key = bytes.fromhex(key_hex)

cipher = AES.new(key, AES.MODE_CFB, segment_size=segment_size)

padded_data = pad(data, 16, style='pkcs7')

ct_bytes = cipher.encrypt(padded_data)

print(f"Ciphertext: {ct_bytes.hex()}")
print(f"IV: {cipher.iv.hex()}")

# Part 2 end
print('\n-------\n')
# Part 3

from Crypto.Cipher import ChaCha20

try:
    nonce_hex = '00d688c8e8c09ef8'
    key_hex = '5aca1416d3d57f0febffa452af34a538fde85303978ca5d0811a5b3be1b0a8c3'
    ciphertext_hex = '9b4b9cedd82076e1277e6b53dfbbd056164a56fe096fe5a7ca001620'

    nonce = bytes.fromhex(nonce_hex)
    key = bytes.fromhex(key_hex)
    ct_bytes = bytes.fromhex(ciphertext_hex)

    cipher = ChaCha20.new(key=key,nonce=nonce)

    plaintext = cipher.decrypt(ct_bytes)
    print("Message: " + plaintext.decode('ascii'))

except (ValueError, KeyError):
    print('Incorrect decryption')