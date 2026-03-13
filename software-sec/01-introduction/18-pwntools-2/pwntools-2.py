"""
Problem: Software 18 - Pwntools 2

Category: Software Security

Description: This script solves a time-constrained packing challenge using pwntools. 
The server presents 100 consecutive tasks where it provides a hexadecimal number 
and an architecture size (32-bit or 64-bit). The goal is to parse this data, 
convert it, and send back the raw packed bytes (Little Endian) within 30 seconds. 
It highlights the importance of network synchronization (`recvuntil`) and raw 
byte transmission (`send` vs `sendline`).

Algorithm:
- Point 1: Establish a remote connection to the challenge server using `pwntools`.
- Point 2: Receive the welcome banner and send the start character 'a' to begin.
- Point 3: Iterate through a loop 100 times for each challenge step.
- Point 4: Use `recvuntil()` to skip filler text and precisely extract the target hexadecimal string and the architecture type.
- Point 5: Convert the extracted hexadecimal string into a Python integer using `int(num_str, 16)`.
- Point 6: Pack the integer into raw bytes using `p32()` or `p64()` (Little Endian by default) based on the parsed architecture.
- Point 7: Send the packed raw bytes back to the server using `send()` (avoiding `sendline()` to prevent sending corrupting `\n` bytes).
- Point 8: After successfully completing all 100 steps, use `recvall()` to capture and print the final flag.

"""

from pwn import *

def main():
    HOST = "software-18.challs.olicyber.it"
    PORT = 13001
    r = remote(HOST, PORT)

    data = r.recv(1024)
    print(data.decode('utf-8')) 
    r.sendline(b'a')

    for x in range(100):

        print(f'Step {x}.')
        
        r.recvuntil(b'restituiscimi ')

        num_str = r.recvuntil(b' ').strip().decode('utf-8')
        
        r.recvuntil(b'packed a ')

        pack_type = r.recvuntil(b'bit').decode('utf-8')
        num_bigint = int(num_str, 16)
        
        print(f"{num_str} in a {pack_type}-bit")

        if pack_type == '32-bit':
            to_send = p32(num_bigint)
        else:
            to_send = p64(num_bigint)
        
        print(f'Sending {to_send}')
        r.send(to_send)

    # Capture the flag
    text = r.recvall()
    print(text.decode('utf-8'))

if __name__ == "__main__":
    main()