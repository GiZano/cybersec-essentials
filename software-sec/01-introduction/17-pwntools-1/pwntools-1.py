"""
Problem: Software 17 - Pwntools 1

Category: Software Security

Description: Introduction to the 'pwntools' library for writing exploit scripts. 
The challenge involves interacting with a remote socket, parsing dynamically 
generated arrays of numbers (including negative integers), calculating their sum, 
and sending the result back to the server. This process must be repeated 10 times 
in a loop to retrieve the final flag.

Algorithm:
- Point 1: Import the 'pwn' library and establish a remote connection using 'remote(HOST, PORT)'.
- Point 2: Receive the initial server banner and send the start character (e.g., 'a').
- Point 3: Create a loop to handle the 10 consecutive arithmetic challenges.
- Point 4: Read the string containing the numbers and use Regex ('-?\d+') to extract all valid integers, including negative ones.
- Point 5: Convert the extracted strings to integers and calculate their sum.
- Point 6: Convert the sum back to a string, encode it to bytes, and send it back using 'sendline()'.
- Point 7: Receive and print the final flag after exiting the loop.

"""

from pwn import *
import re


def main():
    HOST = "software-17.challs.olicyber.it"
    PORT = 13000
    r = remote(HOST, PORT)

    data = r.recv(1024)
    
    r.sendline(b'a')
    for x in range(10):
        text = r.recvline()
        print(text.decode('utf-8'))

        numbers = r.recvline()
        to_sum = numbers.decode('utf-8')

        print(to_sum)

        pieces = re.findall(r'-?\d+', to_sum)

        print(pieces)

        to_sum = [int(x) for x in pieces]

        total = sum(to_sum)

        text = r.recv(1024)
        print(text.decode('utf-8'))
        
        print(f"Sending: {total}")
        r.sendline(str(total).encode())

    # Capture the flag
    text = r.recvall()
    print(text.decode('utf-8'))

if __name__ == "__main__":
    main()