# Problem: Software 7 - Stack 1

**Category:** Software Security

**Description:**
Introduction to Stack Strings. The binary hides the flag by avoiding the use of the `.rodata` section. Instead, the string is dynamically constructed at runtime by moving individual characters (bytes) directly into local stack variables. This evades static string analysis tools like `strings`.

## Algorithm

1. Load the binary into **Ghidra** and navigate to the `main` function.
2. Observe the C pseudo-code or Assembly listing for a long sequence of hardcoded byte assignments to local variables.
3. Switch to the Listing View (Assembly) to see the exact hexadecimal values being moved (`MOV`) onto the stack (`RBP - offset`).
4. Read the hex values in order and convert them to ASCII to reconstruct the dynamically generated flag.