# Problem: Software 5 - Strings 2

**Category:** Software Security

**Description:**
Second iteration of string extraction challenges. In this binary, the flag is likely stored in a non-standard ASCII format (e.g., wide characters, or an array of individual hex bytes), effectively bypassing basic terminal tools like `strings`. The solution requires static analysis using a decompiler to reconstruct the memory layout.

## Algorithm

1. Load the ELF binary into the **Ghidra** decompiler and run the initial Auto-Analyze.
2. Locate the `main` function within the Symbol Tree and examine the C pseudo-code.
3. Identify the target variable or array that holds the obscured flag data.
4. Double-click the variable to jump to its raw memory address in the Listing view (e.g., `.rodata` section).
5. Extract the raw hexadecimal bytes and translate them into human-readable ASCII to reconstruct the flag.