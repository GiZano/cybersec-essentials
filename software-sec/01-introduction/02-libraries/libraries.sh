#!/bin/bash
# 
# Problem: Software 02 - Libraries
# Category: Software Security
# 
# Description: Understand dynamic linking in Linux ELF binaries. The script uses the 'ldd' command
# to list all the shared libraries (.so files) required by the executable to run, revealing a 
# suspiciously named library that acts as the flag.
# 
# Algorithm:
# - Run the 'file' command to verify if the binary is dynamically linked.
# - Run the 'ldd' command to print shared object dependencies.
# - Inspect the output for anomalous or custom library names injected by the challenge author.
# 

echo -e '\n=== Basic Analysis ===\n'
file ./sw-02

echo -e '\n=== Shared Libraries Analysis (ldd) ===\n'
# Key command
ldd ./sw-02

echo -e '\n[*] Hint: Look at the output of ldd. Some libs are very strange...'