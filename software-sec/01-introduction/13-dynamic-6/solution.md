# Problem: Software 13 - Dynamic 6 

**Category:** Software Security

**Description:**
Learn how to use the GDB `print` command to inspect CPU registers with specific data formats. The binary loads a hidden value into the `$rax` register and triggers a `SIGTRAP`. The challenge requires reading this value as a signed decimal integer.

## Algorithm

1. Run the binary inside GDB (`gdb ./sw-13`).
2. Start the execution (`run`) and wait for the `int 3` breakpoint to hit.
3. Use the command `print/d $rax` to print the content of the RAX register as a signed decimal number.
4. Extract the numeric value, drop the algebraic sign (if negative), and wrap it in the `flag{}` format.