# 🔐 What The Hash

**What The Hash** is a Python-based CLI tool that helps you **identify and crack unknown hashes** using `hashid` and `hashcat`.

It’s fast, beginner-friendly, and perfect for **entry-level cybersecurity learners**, **CTF players**, and anyone exploring password cracking workflows.

---

## 🎨 ASCII Art

/ )/ )( \ / )( ( / )( ( ) ( ( ) / (( / /) _) ) / () _) _)_/ _/() _/(___)

🔓 What The Hash by [Your Name] 🔓

yaml
Copy
Edit

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
- `hashid` library:
```bash
pip install hashid
hashcat:

bash
Copy
Edit
sudo apt install hashcat
A wordlist:
Default: /usr/share/wordlists/rockyou.txt
(Make sure it exists on your system)

📦 Usage
bash
Copy
Edit
python3 whatthehash.py
🔧 Custom Wordlist Support
By default, the script uses:

python
Copy
Edit
wordlist = "/usr/share/wordlists/rockyou.txt"
To use your own wordlist, replace the above line with:

python
Copy
Edit
wordlist = "/path/to/your/wordlist.txt"
📁 Project Structure
python
Copy
Edit
what-the-hash/
├── whatthehash.py     # Main script
├── README.md          # This file
├── target_hash.txt    # Temporary file (auto-deleted)
🧠 Concepts Covered
Hash identification (MD5, SHA1, NTLM, etc.)

Wordlist-based password attacks

Python automation using subprocess

CLI scripting and logic handling

Mapping hash types to hashcat modes

👨‍💻 Author
Your Name
🔗 GitHub
🔗 LinkedIn
📫 Email: your.email@example.com

⚠️ Disclaimer
This tool is intended for educational and ethical use only.
Do not use it on systems you do not own or have explicit permission to test.

yaml
Copy
Edit

---

✅ Now just:
- Replace `[Your Name]`, GitHub/LinkedIn/email with yours
- Save this file as `README.md` in your project folder
- Push it to GitHub

Let me know if you want a `LICENSE` file or project icon to go with it!
