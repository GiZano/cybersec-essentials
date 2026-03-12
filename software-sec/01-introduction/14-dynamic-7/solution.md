# Problem: Software 14 - Dynamic 7 (GDB Examine)

**Category:** Software Security

**Description:**
Learn to inspect raw memory in GDB using the `x` (examine) command. Unlike `print`, which evaluates expressions or registers, `x` dereferences a memory address and formats its contents. The binary hides a float value on the stack at the address `$rbp-4`.

## Algorithm

1. Run the binary inside GDB (`gdb ./sw-14`).
2. Start the execution (`run`) and wait for the `int 3` breakpoint.
3. Use the command `x/f $rbp-4` to examine memory. 
   - `x`: Examine memory.
   - `f`: Format as a floating-point number.
   - `$rbp-4`: The target memory address on the stack.
4. Extract the integer portion of the floating-point number and wrap it in `flag{}`.