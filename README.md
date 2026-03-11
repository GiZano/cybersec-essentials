<div align="center">

# 🛡️ CyberSec Essentials & CTF Training
### Cybersecurity | Ethical Hacking | Problem Solving

> A personal toolbox and collection of scripts developed while solving CTF challenges on the **OliCyber** training platform.
> <br>**Status:** Actively training for the OliCyber Territorial Selections. 🎯

<br>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Wireshark](https://img.shields.io/badge/Wireshark-1679A7?style=for-the-badge&logo=wireshark&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white)


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

</div>

## 🛠️ My Tools (Quick Links)
Here are the universal and interactive scripts, ready to be executed during CTF competitions:

### 🌐 Web Security
* [🕷️ Simple Web Spider](utils/spider.py) - DFS crawler to explore websites and find hidden flags within HTML anchors.
* [💉 SQLi Blind/Time-Based Automator](utils/sqli_automator.py) - Script to extract flags character by character exploiting response times (`SLEEP`) or boolean inferences.

### 🔐 Cryptography
* [🧮 Modular Arithmetic Toolkit](utils/mod_math_tool.py) - Interactive CLI to calculate the Extended Euclidean Algorithm (EGCD) and Modular Multiplicative Inverse. (Crucial for RSA!).
* [💥 Single-Byte XOR Brute-Forcer](utils/xor_bruteforce.py) - Script that tests all 256 possible keys against a ciphertext, extracting only human-readable text (UTF-8 safe).
* [🔄 Universal Decoder (Base64/Hex/BigInt)](utils/decoder.py) - Ready-to-use snippets for fast conversions between bytes, hexadecimal, Base64, and giant integers (Big Endian).

---

## 📖 Overview

Welcome to my personal Cybersecurity repository. This is not just a collection of solutions, but a custom-built toolkit containing Python scripts, automated exploits, and analysis tools I wrote to solve Capture The Flag (CTF) challenges.

Currently, this repository is focused on my preparation for the **OliCyber** (Italian Cybersecurity Olympics) training platform, helping me transition from a tool-user to a tool-builder.

### 🎯 Core Goals

* **⚙️ Automation:** Writing scripts to automate repetitive tasks, from brute-forcing to decoding algorithms.
* **🧠 Deep Understanding:** Understanding the underlying math and logic of vulnerabilities instead of relying solely on automated external tools.
* **🧰 Personal Toolkit:** Building a reliable, well-documented library of code snippets to reuse during timed, competitive CTF environments.

---

## 🛠 Tech Stack & Concepts

| Category | Technologies & Focus Areas |
| :--- | :--- |
| **Languages** | Python 3.x, Bash |
| **Cryptography** | RSA, AES, XOR, Custom Ciphers, Encoding/Decoding techniques |
| **Web Security** | SQL Injection, XSS, Command Injection, Directory Traversal |
| **Network Security** | Packet Analysis (PCAP), Socket Programming, Port Scanning |
| **Software Security** | Reverse Engineering basics, Binary exploitation concepts |

---

## 📂 Repository Structure & Solutions

To maintain a clean and readable workspace, the specific solutions and script catalogs are separated by category. **Navigate to each folder to view its dedicated `README.md` and the list of solved challenges.**

```text
cybersec-essentials/
├── cryptography/         # Scripts for ciphers, hashing, and decryption
├── misc/                 # Miscellaneous challenges (OSINT, Steganography, etc.)
├── network-sec/          # Packet analysis and network exploitation tools
├── software-sec/         # Reverse engineering and binary analysis scripts
├── web-security/         # Web exploitation and automation scripts
├── utils/                # Shared helper modules
│   └── template.py       # Base boilerplate for fast CTF script creation
├── .gitignore            # Git ignore rules
├── requirements.txt      # Python dependencies for the scripts
└── README.md             # This documentation file
```

---

<br><br>
<div align="center">
Made with ❤️ and lots of coffee ☕<br>
© 2026 Giovanni Zanotti. All Rights Reserved.
</div>