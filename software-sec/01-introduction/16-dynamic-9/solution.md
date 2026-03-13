# Problem: Software 16 - Dynamic 9 (GDB Memory Patching)

**Category:** Software Security

**Description:**
Introduction to dynamic memory manipulation using GDB. The objective is to pause the binary execution during a `sleep` call and manually overwrite the value of a global variable (`tochange`) in memory. If the variable is successfully patched with the expected "magic" value before execution resumes, the program calculates and prints the flag.

## Algorithm

1. Load the binary in GDB: `gdb ./sw-16`.
2. Disassemble the `main` function to locate the `sleep` call.
3. Set a manual breakpoint exactly at the `call sleep@plt` instruction (e.g., `b *main+81`).
4. Start the execution with `run`. The program will print the target address/variable name and the expected value before hitting the breakpoint.
5. Once halted, identify the memory address of the global variable using `p &tochange`.
6. Overwrite the memory using the `set` command. You can use explicit addressing: `set {unsigned long}0x404038 = 0xdeadc0debadc0ffe` or direct variable assignment: `set var tochange = 0xdeadc0debadc0ffe`.
7. Resume execution with `continue`.
8. The program will validate the patched memory and output the flag to the console.