## 🛠️ Tools & Environment Setup

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