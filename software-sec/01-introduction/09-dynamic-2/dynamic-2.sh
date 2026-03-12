#!/bin/bash
# 
# Problem: Software 9 - Dynamic 2
# Category: Software Security
# 
# Description: Advanced dynamic analysis using system calls. Unlike ltrace which hooks 
# shared library calls, this challenge requires 'strace' to monitor direct interactions 
# between the binary and the Linux kernel. The flag is leaked as an argument to the 
# 'openat' system call.
#
# Algorithm:
# - Run 'file' to understand the binary context.
# - Grant execution permissions with 'chmod +x'.
# - Execute the binary through 'strace' to hook and log all kernel system calls.
# - Inspect the output specifically for the 'openat()' system call to extract the flag.
#

echo -e '\n=== Basic Analysis ===\n'
file ./sw-09

echo -e '\n=== Make sw-09 executable (chmod +x) ===\n'
chmod +x ./sw-09

echo -e '\n=== Dynamic System Calls Analysis (strace) ===\n'
strace ./sw-09

echo -e '\n[*] Hint: Read the system calls, look for openat(... "flag{...}" ...)!'