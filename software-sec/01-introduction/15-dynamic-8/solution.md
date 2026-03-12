# Problem: Software 15 - Dynamic 8 (GDB Manual Breakpoints)

**Category:** Software Security

**Description:**
This challenge introduces manual breakpoint management and memory inspection in GDB, emphasizing the importance of Stack Frames and architecture-specific data types. The goal is to halt execution exactly before a library function (`puts`) is called within `main`, ensuring the base pointer (`$rbp`) still references the `main` stack frame. Additionally, it highlights the necessity of using the correct memory size formatting (`g` for an 8-byte 64-bit `unsigned long`) when dereferencing stack variables.

## Algorithm

1. Load the binary into the GNU Debugger using `gdb ./sw-15`.
2. Analyze the `main` function using the `disassemble main` command.
3. Locate the `call puts@plt` instruction and identify its specific offset (e.g., `<+95>`).
4. Set a manual breakpoint exactly at that instruction using `b *main+95` (or the absolute hex address).
5. Start the program execution with `run` and wait for the breakpoint to trigger.
6. Once execution halts, examine the 8-byte `unsigned long` variable on the stack using the Examine command with the Giant word formatter: `x/1xg $rbp-0x8`.
7. Extract the raw hexadecimal value (e.g., `0x0000002823a0c041`), strip the `0x` prefix and leading zeros, and wrap it in the `flag{}` format.

**Flag:** `flag{2823a0c041}`