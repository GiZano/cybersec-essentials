#!/bin/bash
# 
# Problem: Software 11 - Dynamic 4
# Category: Software Security
# 
# Description: Analyzes a multi-process binary. The program uses the fork() 
# system call to create a child process, which then attempts to open the flag. 
# Standard tracing only monitors the parent process. We use 'strace -f' to follow 
# child processes and capture the 'openat' system call executed by the child.
#
# Algorithm:
# - Run 'file' to check binary properties.
# - Grant execution permissions with 'chmod +x'.
# - Run 'strace -f' to trace system calls across both parent and child processes.
# - Search the output for the 'openat' (or 'open') call containing the flag string.
#

echo -e '\n=== Basic Analysis ===\n'
file ./sw-11

echo -e '\n=== Make sw-11 executable (chmod +x) ===\n'
chmod +x ./sw-11

echo -e '\n=== Dynamic System Calls Analysis following forks (strace -f) ===\n'
strace -f ./sw-11

echo -e '\n[*] Hint: Analyze the output and search for openat(... "flag{..." ...)'