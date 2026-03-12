#!/bin/bash
# 
# Problem: Software 04 - Strings 1
# Category: Software Security
# 
# Description: Simulates a classic CTF reverse engineering challenge where a binary
# checks user input against a hardcoded string. The script uses the 'strings' 
# utility to extract all printable character sequences from the compiled ELF file
# to find the hidden password/flag.
#
# Algorithm:
# - Run the 'file' command to understand the basic properties of the binary.
# - Run the 'strings' command to dump all human-readable ASCII sequences.
# - Pipe the output to 'grep' (optional but suggested) to filter out noise.
#

echo -e '\n=== Basic Analysis ===\n'
file ./sw-04

echo -e '\n=== Strings in the file ===\n'
strings ./sw-04

# --- PRO TIP ---
echo -e '\n=== Flag (grep) ===\n'
strings ./sw-04 | grep "flag{"

echo -e '\n[*] Hint: Scroll through the strings. Look for something that resembles a flag or a password!'