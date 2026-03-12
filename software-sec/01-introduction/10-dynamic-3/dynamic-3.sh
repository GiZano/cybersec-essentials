#!/bin/bash
# 
# Problem: Software 10 - Dynamic 3
# Category: Software Security
# 
# Description: Focuses on filtering dynamic analysis output. The binary makes 
# numerous library calls, making standard ltrace output too noisy. We use 
# ltrace with the '-e' flag to hook and trace only the specific 'access' 
# function, which takes the flag as its argument.
#
# Algorithm:
# - Run 'file' to analyze the binary.
# - Make the binary executable using 'chmod +x'.
# - Run 'ltrace -e access' to filter the output and trace exclusively the 'access' library call.
# - Extract the flag passed directly as the argument.
#

echo -e '\n=== Basic Analysis ===\n'
file ./sw-10

echo -e '\n=== Make sw-10 executable (chmod +x) ===\n'
chmod +x ./sw-10

echo -e '\n=== Dynamic Library Calls Analysis with filter (ltrace -e) ===\n'
ltrace -e access ./sw-10

echo -e '\n[*] Hint: It is not hard, there is only one call to analyze!'