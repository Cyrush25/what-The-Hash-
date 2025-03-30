# 🔐 What The Hash

What The Hash is a Python-based CLI tool that helps you **identify and crack unknown hashes** using `hashid` and `hashcat`.

It’s fast, user-friendly, beginner-friendly, and perfect for **entry-level cybersecurity learners**, **CTF players**, and anyone exploring password cracking workflows.

---

## ✨ Features

- 🧠 Auto-identifies hash type(s) using `hashid`
- 🧩 Maps top 5 guesses to appropriate `hashcat` modes
- 🔓 Cracks the hash using a **customizable wordlist** (default: `rockyou.txt`)
- 🎯 Stops at the first successful crack
- 🎨 Includes ASCII art for fun CLI branding
- 🛡️ Error-handled for invalid modes or uncrackable hashes

---

## 🚀 How It Works

1. You provide a single hash
2. The tool identifies likely hash types
3. It maps each to hashcat mode IDs
4. Tries cracking with `hashcat` and the selected wordlist
5. Shows the cracked password (if found)

---

## 🛠️ Requirements

- Python 3.x
- `hashid` library  
  ```bash
  pip install hashid
