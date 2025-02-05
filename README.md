# Brute Force Password Cracker

## 📌 Overview
This tool attempts to crack **MD5-hashed passwords** using a **multi-threaded brute force approach**. It tests different character combinations until the correct password is found.

## 🚀 Features
✔ **Multi-threaded for speed** – Faster brute force execution  
✔ **User-defined max password length** – Controls complexity  
✔ **Optimized workload distribution** – Efficient password testing  
✔ **Early termination** – Stops as soon as the correct password is found  
✔ **Time tracking** – Measures performance

## 📦 Installation
### **1️⃣ Install Python (If not installed)**
Ensure you have Python 3 installed. Check using:
```bash
python3 --version
```
If not installed, download it from [python.org](https://www.python.org/).

### **2️⃣ Clone the repository**
```bash
git clone https://github.com/yourusername/brute-force-cracker.git
cd brute-force-cracker
```

## 🛠 Usage
### **Run the script**
```bash
python brute_force_cracker.py
```

### **Provide Input**
1. Enter the **MD5 hash** of the password to crack.
2. Set the **maximum password length**.

### **Example Run**
```
Enter MD5 hash to crack: 5d41402abc4b2a76b9719d911017c592
Enter maximum password length: 5
[+] Password found: hello
[+] Time taken: 2.3 seconds
```

## 🛡️ Limitations
- **Brute force can take a long time** for complex passwords.
- **Only works with MD5 hashes** (can be expanded for SHA256, SHA512, etc.).

## ⚠️ Disclaimer
This tool is for **educational and security research purposes only**. **Unauthorized use is illegal**. Ensure you have **explicit permission** before using it.

🔒 **Use responsibly!**

