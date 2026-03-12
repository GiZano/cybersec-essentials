#!/bin/bash
# 
# Problem: Software 03 - Sections
# Category: Software Security
# 
# Description: Explores the internal structure of an ELF binary by inspecting its sections. 
# The script uses 'objdump' to list all sections and then extracts the raw content 
# (hexadecimal and ASCII) of a specific, non-standard "secret" section containing the flag.
# 
# Algorithm:
# - Run 'file' to confirm the binary format.
# - Run 'objdump -h' to print the section headers and identify anomalous sections.
# - Run 'objdump -s -j <section_name>' to display the full contents of the target section.
# 

echo -e '\n=== Basic Analysis ===\n'
file ./sw-03

echo -e '\n=== ELF Sections (-h) ===\n'
objdump -h ./sw-03

echo -e '\n=== Super Secret Section Content (-s -j) ===\n'
objdump -s -j .super-secret-section ./sw-03

echo -e '\n[*] Hint: Look at the ASCII column on the right of the hex dump. The flag is hiding there!'