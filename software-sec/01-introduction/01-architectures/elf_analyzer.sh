#!/bin/bash
# 
# Problem: Software 01 - Architectures
# Category: Software Security
# 
# Description: Introduction to Reverse Engineering and Pwn. The script analyzes a compiled 
# Linux ELF binary to determine its target CPU architecture by inspecting its metadata 
# and internal headers.
# 
# Algorithm:
# - Run the 'file' command to get a high-level summary of the executable (bitness, linking, architecture).
# - Run 'readelf -h' to parse the raw ELF header and explicitly read the 'Machine' field.
# - Extract the architecture name, convert it to lowercase, and format it as the final flag (e.g., flag{x86-64}).
# 

echo -e '\n=== Basic Analysis ===\n'
file ./sw-01

echo -e '\n=== Header Analysis ===\n'
readelf -h ./sw-01

echo -e '\n[*] Hint: Read the "Machine" field. The flag uses the lowercase architecture name already found in the first output (e.g., flag{x86-64})!'