# Cybersec Cheat Sheet

- <a href='#env'>🛠️ Tools & Environment Setup</a>
- <a href='#gdb'>🐞 GDB (GNU Debugger)</a>
- <a href='#ghidra'>🐉 Ghidra</a>
- <a href='#static'>🛠️ Basic Static Analysis & Linux Commands</a>


## <p id='gdb'>🐞 GDB (GNU Debugger)</p>

A quick reference guide for the most common GDB commands used during dynamic analysis and reverse engineering.

### 🏃‍♂️ Execution Control
* **`run`** (or `r`): Starts the execution of the program.
* **`continue`** (or `c`): Resumes execution after hitting a breakpoint.
* **`stepi`** (or `si`): Executes exactly *one* machine instruction (steps into function calls).
* **`nexti`** (or `ni`): Executes exactly *one* machine instruction (steps over function calls).
* **`quit`** (or `q`): Exits GDB.

### 🛑 Breakpoints
* **`break *0x401173`** (or `b`): Sets a breakpoint at a specific memory address.
* **`break main`**: Sets a breakpoint at the start of a function.
* **`break *main+95`**: Sets a breakpoint at a specific offset from a function's start.
* **`info breakpoints`** (or `i b`): Lists all active breakpoints.
* **`delete 1`** (or `d 1`): Deletes breakpoint number 1.

### 🔍 Inspection & Analysis
* **`disassemble main`** (or `disas`): Shows the assembly code for a function.
* **`info registers`** (or `i r`): Dumps the current state of all CPU registers.
* **`print`** (or `p`): Evaluates and prints expressions or registers.
  * `p/x $rax`: Prints RAX in hexadecimal.
  * `p/d $rax`: Prints RAX in signed decimal.
  * `p &tochange`: Prints the memory address of a global variable.
* **`x` (Examine)**: Inspects raw memory at a specific address using the syntax `x/nfu address`.
  * **n** (Count): How many elements to display (default is 1).
  * **f** (Format): `x` (hex), `d` (decimal), `f` (float), `s` (string), `i` (instruction).
  * **u** (Size): `b` (byte, 1), `h` (halfword, 2), `w` (word, 4), `g` (giant, 8).
  * *Examples:*
    * `x/1xg $rbp-0x8`: Examine 1 Giant word (8 bytes) in hex.
    * `x/s 0x402000`: Examine memory as an ASCII string.
    * `x/5i $rip`: Examine the next 5 assembly instructions.

### ✍️ Memory & Register Modification
* **`set $rax = 0`**: Changes the value of a CPU register.
* **`set var tochange = 0xdeadbeef`**: Modifies the value of a known variable.
* **`set {unsigned long}0x404038 = 0x1234`**: Overwrites memory at a specific address, casting it to a specific data type size.

---

## <p id='static'>🛠️ Basic Static Analysis & Linux Commands</p>
Before firing up a debugger or decompiler, these command-line tools help you understand the target binary's structure, architecture, and dependencies.

* **`file <binary>`**: Determines the file type, architecture (e.g., 32-bit vs 64-bit), and whether it's statically or dynamically linked, or stripped.
* **`strings <binary>`**: Extracts and prints all printable character sequences from the file.
  * `strings -n 8 <binary>`: Only show strings of at least 8 characters.
  * `strings -t x <binary>`: Show the hexadecimal offset (memory location) of each string.
* **`ldd <binary>`**: Prints the shared libraries (shared objects) required by the program (e.g., `libc.so.6`).
* **`readelf <binary>`**: Displays detailed information about ELF (Executable and Linkable Format) files.
  * `readelf -h <binary>`: Shows the ELF header (entry point, architecture).
  * `readelf -S <binary>`: Lists all sections (e.g., `.text`, `.data`, `.rodata`).
  * `readelf -s <binary>`: Displays the symbol table (functions, global variables).
* **`objdump <binary>`**: Displays information from object files.
  * `objdump -d -M intel <binary>`: Disassembles the executable sections (`.text`) using Intel syntax (easier to read than AT&T).

---

## <p id='ghidra'>🐉 Ghidra</p>
Ghidra is your primary tool for deep static analysis and decompilation. Here are the most critical shortcuts and concepts.

### ⌨️ Essential Shortcuts
* **`L` (Rename Label/Variable)**: The most important key! Use it in the Decompile view to rename obscure variables (e.g., change `local_10` to `user_input`) or functions.
* **`T` (Change Data Type)**: Allows you to force a variable into a specific type (e.g., change an `int` to an `unsigned long` or a `char *`).
* **`G` (Go To)**: Jump to a specific memory address or symbol/function name.
* **`Ctrl + Shift + E` (Search Strings)**: Opens the defined strings window to find hardcoded text (like error messages or flags).
* **`;` (Add Comment)**: Add your own notes directly into the Assembly or Decompiled C code.

### 🧠 Understanding Ghidra's Decompilation
* **The Stack & Local Variables**: In x86_64, local variables are stored on the Stack, usually at negative offsets from the Base Pointer (`RBP`). 
  * If you see assembly like `mov [rbp-0x10], rax`, Ghidra will often translate this in the Decompile view as a variable named **`local_10`** or **`local_18`** (depending on the exact byte offset).
* **Parameters**: Function arguments passed via registers (`RDI`, `RSI`, `RDX`, etc. in x86_64) are usually named `param_1`, `param_2`, etc. Rename them as soon as you figure out what they do!
* **Global Variables**: Found in sections like `.data` or `.bss`, often represented by their absolute memory address (e.g., `DAT_00404038`). Rename them with `L` once you identify their purpose.
* **Stack Strings**: If you see a long sequence of individual characters being moved into variables (e.g., `local_10 = 'f'; local_11 = 'l'; local_12 = 'a';`), the binary is dynamically building a string on the stack to hide it from the `strings` command.

---

## <p id='env'>🛠️ Tools & Environment Setup</p>

This repository contains write-ups and scripts for Software Security challenges. To run the analyses and scripts, you need to set up the following reverse engineering and debugging tools on a Linux environment (Ubuntu/Debian or WSL).

### 1. Basic Static Analysis Tools
Most of these are included in the standard 'binutils' package. They are essential for inspecting binary headers, sections, and embedded ASCII data.
* **Tools:** 'file', 'strings', 'objdump'
* **Installation:**
```bash
sudo apt update
sudo apt install file binutils
```

### 2. Dynamic Analysis & Tracing
Used to monitor the behavior of compiled binaries at runtime without a debugger.
* **ltrace:** Intercepts dynamic library calls (e.g., 'libc' functions like 'puts', 'open', 'strcmp').
* **strace:** Monitors direct interactions between the binary and the Linux Kernel (System Calls like 'openat', 'mmap').
* **Installation:**
```bash
sudo apt install ltrace strace
```

### 3. Debugging (GDB)
The GNU Debugger is the core tool for runtime memory inspection, register analysis, and manual breakpoints.
* **Tool:** 'gdb'
* **Installation:**
```bash
sudo apt install gdb
```

### 4. Advanced Static Analysis (Ghidra)
Ghidra is a powerful reverse engineering suite developed by the NSA, used for disassembling and decompiling ELF binaries into C pseudo-code. It requires a specific version of Java.

**Step A: Install Java (OpenJDK 21+) and Unzip**
```bash
sudo apt install openjdk-21-jdk unzip wget
```

**Step B: Download and Extract Ghidra**
*(Note: Check the official GitHub repository for the latest release link)*
```bash
# Download the zip file
wget https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_11.0.3_build/ghidra_11.0.3_PUBLIC_20240410.zip

# Extract it
unzip ghidra_*_PUBLIC_*.zip

# Run it
cd ghidra_*_PUBLIC/
./ghidraRun
```
*(Tip: On the first run, Ghidra might ask for the JDK path. You can find it by running: 'dirname $(dirname $(readlink -f $(which javac)))')*

### 5. Scripting
We use Python 3 to write solvers, automate XOR decryptions, and parse hexadecimal dumps.
* **Installation:**
```bash
sudo apt install python3
```

