# Problem: Software 12 - Dynamic 5

**Category:** Software Security

**Description:**
Introduction to runtime debugging with `gdb`. The binary loads pieces of the flag directly into the CPU registers and then triggers a software breakpoint (`int 3` / `SIGTRAP`). The objective is to catch the interrupt using the debugger and inspect the hardware state.

## Algorithm

1. Load the binary into the GNU Debugger using `gdb ./sw-12`.
2. Start the execution with the `run` command.
3. Wait for the `SIGTRAP` signal caused by the embedded `int 3` instruction.
4. Execute `info registers` to dump the current state of the CPU.
5. Extract the hexadecimal values from the first three general-purpose registers (`rax`, `rbx`, `rcx`).
6. Concatenate the hex strings (excluding the `0x` prefix) to form the flag.