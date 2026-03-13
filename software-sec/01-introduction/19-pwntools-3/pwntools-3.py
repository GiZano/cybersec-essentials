"""
Problem: Software 19 - Pwntools 3

Category: Software Security

Description: This challenge introduces the `ELF` module in pwntools, which allows 
for dynamic inspection of binary files. The server requests the hexadecimal memory 
addresses of specific functions (e.g., `main`, `dead`, `cafe`) within a strict time 
limit (20 steps in 10 seconds). The script must load the local binary, dynamically 
resolve the requested symbols, format them as hexadecimal strings, and send them 
back to the server.

Algorithm:
- Point 1: Import the `ELF` class from pwntools and load the local binary `sw-19`.
- Point 2: Implement a conditional connection using `args.REMOTE` to switch between local testing (`process`) and remote exploitation (`remote`).
- Point 3: Receive the initial server banner and send the start character 'a'.
- Point 4: Loop 20 times to handle all the requests within the time limit.
- Point 5: Use `recvuntil()` to parse the exact name of the requested function, stripping unwanted characters like `:`.
- Point 6: Use `exe.sym[func]` to dynamically resolve the function's integer address from the ELF symbol table.
- Point 7: Convert the integer address to a hexadecimal string using Python's `hex()` function.
- Point 8: Send the formatted address string back to the server using `sendline()`.
- Point 9: After 20 successful iterations, capture and print the final flag using `recvall()`.

"""

from pwn import *

exe = ELF("./sw-19")

def main():
    
    if args.REMOTE:
        p = remote("software-19.challs.olicyber.it", 13002)
    else:
        p = process([exe.path])

    data = p.recv(1024)
    print(data.decode('utf-8'))
    p.send(b'a')

    for x in range(20):

        print(f"Step {x}.")

        task = p.recvuntil(b'-> ')
        print(task)
        func = p.recvuntil(b':').strip(b':').decode('utf-8')
        print(func)

        address = hex(exe.sym[func])

        print(f'Address of {func} -> {address}')

        p.sendline(address.encode())
    
    # Capture the flag
    text = p.recvall()
    print(text.decode('utf-8'))

if __name__ == "__main__":
    main()