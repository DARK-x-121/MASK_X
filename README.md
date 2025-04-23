# MASK X 🎭 - Advanced Phishing Link Masking Tool

![MASK X Banner](https://via.placeholder.com/1200x300.png?text=MASK+X+-+Phishing+Link+Masker)  
*Hide phishing links behind realistic URLs with social engineering magic!*

## 🌟 Introduction

**MASK X** is a powerful Python-based tool designed for ethical hackers, security researchers, and penetration testers to learn and understand phishing link masking techniques. This tool allows you to mask any phishing URL (e.g., a fake login page) behind a legitimate-looking domain (e.g., `https://facebook.com`) with social engineering words to make it appear trustworthy. Built with simplicity and functionality in mind, MASK X is perfect for educational purposes and authorized testing environments.

> **⚠️ Disclaimer**: This tool is for educational and ethical testing purposes only. Using it for illegal activities, such as phishing real users without consent, is strictly prohibited and may lead to legal consequences (e.g., violation of India’s IT Act Section 66D). Always obtain permission before testing on any system.

## 🛠️ Features

- **Phishing Link Masking**: Converts any phishing URL into a realistic-looking link using a masking domain.
- **Social Engineering**: Add custom social engineering words (e.g., `free-money`, `best-offers`) to make the link more convincing.
- **URL Shortening**: Automatically shortens the phishing URL using the `is.gd` API for a cleaner look.
- **Validation**: Ensures the input URLs start with `http` or `https` to avoid errors.
- **User-Friendly Interface**: Colorful CLI with an ASCII banner for a professional experience.
- **Auto-Stop**: Built-in self-destruct timer to stop the tool after generating the link.

## 📋 Requirements

- **Python 3.x**
- **Termux** (optional, for Android users)
- Required Python libraries:
  - `requests`
  - `colorama


## installation in termux --- 


```
apt update && upgrade
pkg install python
pkg install git
git clone https://github.com/DARK-x-121/MASK_X.git
cd MASK_X
python mask.py
```

thanks for choosing our tool 
   BY DARK 
