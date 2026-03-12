#!/bin/bash
# 
# Problem: Software 8 - Dynamic 1
# Category: Software Security
# 
# Description: Introduction to Dynamic Analysis. The binary attempts to open a file, 
# but it uses the actual flag as the filename argument. By using 'ltrace' to intercept 
# dynamic library calls during execution, we can read the flag directly from the 
# parameters passed to the open() function, bypassing the need for static reversing.
#
# Algorithm:
# - Run 'file' to verify the binary architecture and linking.
# - Grant execution permissions to the binary using 'chmod +x'.
# - Execute the binary through 'ltrace' to hook and log all shared library calls.
# - Inspect the output specifically for the 'open()' function call to extract the flag.
#

echo -e '\n=== Basic Analysis ===\n'
file ./sw-08

echo -e '\n=== Make sw-08 executable (chmod +x) ===\n'
chmod +x ./sw-08

echo -e '\n=== Dynamic Analysis (ltrace) ===\n'
ltrace ./sw-08

echo -e '\n[*] Hint: Read the function calls, look for open("flag{...}")!'