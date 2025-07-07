# 🔐 Password Strength Checker – Prodigy InfoTech Internship Task 3

This Python tool evaluates the strength of a password based on key security criteria. Developed as part of my **Cyber Security Internship** with **Prodigy InfoTech**, it helps users understand how secure their passwords are and how to improve them.

---

## ✅ Features

- Checks for:
  - Minimum length (8 characters)
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- Classifies password as:
  - Weak ❌
  - Moderate ⚠️
  - Strong 💪
- Provides clear feedback on missing criteria
- Lightweight and easy to use

---

## 🚀 How to Use

### 1. Run the Script

```bash
python password_checker.py

- Enter a password when prompted. The tool will:
- Check for length, uppercase, lowercase, numbers, and special characters
- Display which criteria are missing
- Classify the password as ❌ Weak, ⚠️ Moderate, or 💪 Strong

```markdown
---

## 🧪 Sample Output

Enter your password:
Ahmed123

❌ Missing special character ⚠️ Password Strength: Moderate

Enter your password:
Ahmed@123

✅ All criteria met! 💪 Password Strength: Strong

---

## 🧠 What I Learned

- How to validate password strength using Python  
- How to use regular expressions for pattern matching  
- How to give user-friendly feedback in CLI tools  
- The importance of strong passwords in cybersecurity