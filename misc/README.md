# 🏴‍☠️ CTF Survival Guide & Cheatsheet

This document contains a step-by-step method to tackle Capture The Flag (CTF) challenges and a cheatsheet of fundamental commands, divided by category. When facing an empty terminal, panic is your worst enemy: follow the method.

---

## 🌐 1. Web Security (Web)
The goal is to understand how the application handles (or fails to handle) user input and authentication.

* **Basic Reconnaissance:** Browse the site normally. Open DevTools (F12). Check the HTML source (hidden comments?), JavaScript files (logic or API keys?), and cookies.
* **Look for "Secret Doors":** Check `/robots.txt`, `/sitemap.xml`, and `/.git/`. Use tools like **Gobuster** or **Dirb** to discover hidden files or directories (e.g., `admin.php`).
* **Map the Inputs:** Find every point where you can send data: login forms, URL parameters (`?id=1`), and HTTP headers (`User-Agent`).
* **Test for Vulnerabilities (Fuzzing):**
  * Insert `'` everywhere. If the site crashes, you have a **SQL Injection (SQLi)**.
  * Insert `<h1>test</h1>`. If the page renders it, you have **Cross-Site Scripting (XSS)**.
  * Modify parameters (`?page=../../../../etc/passwd`). If you see system files, you have a **Local File Inclusion (LFI)**.
* **Intercept & Manipulate:** Use **Burp Suite** to intercept HTTP requests, modify cookies, and test vulnerabilities like IDOR.

---

## 💻 2. Software Security (Pwn & Reverse Engineering)
You have a binary file and must bend it to your will or understand its secret logic.

* **Binary Profiling:** Use `file <binary>` (for architecture) and `strings <binary>` (for plaintext). Always run `checksec <binary>` to see active defenses (NX, ASLR, Canary).
* **Reverse Engineering:** Open the binary in **Ghidra**. Find the `main` function, rename variables, and look for dangerous functions like `gets()`, `strcpy()`, or `printf(buffer)`.
* **Dynamic Analysis:** Open the program in **GDB**. Set breakpoints, check registers, and inspect the stack.
* **Exploit Calculation:** Find the exact offset for a Buffer Overflow by sending a cyclic pattern, or exploit a Format String (`%p`) to read/write memory.
* **Scripting:** Use **Pwntools** to automate the interaction, bypass ASLR, and inject shellcode or a ROP chain.

---

## 📡 3. Network Security (Network Forensics)
Analyzing a `.pcap` file (traffic capture) to understand what happened on the network.

* **General Statistics:** In **Wireshark**, use *Statistics -> Protocol Hierarchy* for a quick overview of the used protocols.
* **Filter the Noise:** Use filters like `http.request`, `dns`, `ftp`, or `telnet` (plaintext protocols where passwords fly around).
* **Follow Streams:** Right-click an interesting packet -> *Follow -> TCP/HTTP Stream* to read the entire cleaned-up conversation.
* **Data Extraction (Carving):** Go to *File -> Export Objects -> HTTP/SMB* to save all files transferred during the capture to your disk.

---

## 🔐 4. Cryptography (Crypto)
Reverse an encrypted string (ciphertext) by understanding the algorithm or exploiting its weaknesses.

* **Identify the Cipher:** Mixed letters? Classical (Caesar, Vigenère). Base64? Ends with `=`. Random bytes with an attached `.py` file? Modern (RSA, AES, XOR).
* **XOR Properties:** If A XOR B = C, then C XOR B = A. XOR the ciphertext with the known flag format (e.g., `flag{`) to recover part of the key.
* **Mathematical Weaknesses (RSA):** If you have n and e, try factoring n on *factordb.com* to find prime numbers p and q.
* **Tools:** Don't reinvent the wheel, use **CyberChef** for quick conversions and decodings.

---

## 🗂️ 5. Misc & Steganography
The golden rule: **never trust what you see (not even the file extension).**

### Fundamental Tools
* **file / strings / exiftool**: To identify the true nature of the file, extract plaintext, or read metadata (including hidden thumbnails).
* **binwalk**: Scans and extracts hidden or appended files (e.g., a ZIP inside a JPG).
* **steghide**: Tool to extract data from **JPEG** and **BMP** (requires a passphrase, often hidden in the challenge description).
* **zsteg**: Analyzes the least significant bits (LSB) of **PNG** files without needing a password.
* **StegOnline / Aperi'Solve**: Web platforms to visually inspect "Bit Planes" (e.g., Green 0) and reveal hidden messages by altering single pixels.

### ⚙️ Tool Installation (Debian / Ubuntu / Kali)

```bash
# Update repositories
sudo apt update

# Install basic tools (often pre-installed) plus binwalk, steghide, and exiftool
sudo apt install -y file binutils binwalk steghide libimage-exiftool-perl

# Install Ruby and zsteg
sudo apt install -y ruby-full
sudo gem install zsteg

# Install stegano (Python option for LSB analysis)
pip3 install stegano
```

### Stego/Misc Commands Cheatsheet

```bash
# 1. Identify the true file type and search for plaintext
file filename.jpg
strings filename.jpg | tail -n 30
strings filename.jpg | grep -i "flag{"

# 2. Read metadata and extract hidden thumbnails
exiftool filename.jpg
exiftool -b -ThumbnailImage filename.png > thumb.jpg

# 3. Search for appended files and extract them automatically
binwalk -e filename.jpg

# 4. Steganography on JPEG (requires password)
steghide extract -sf filename.jpg

# 5. Steganography on PNG (automatic search across all LSB channels)
zsteg filename.png

# 6. Python alternative for LSB (if zsteg/ruby are unavailable)
stegano-lsb reveal -i filename.png
```