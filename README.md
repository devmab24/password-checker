# 🔐 Password Security Checker

A Python script that checks if your passwords have been compromised in data breaches using the HaveIBeenPwned API. This tool helps you identify weak or compromised passwords to improve your online security.

## 🌟 Features

- **Breach Detection**: Checks passwords against 600+ million compromised passwords from data breaches
- **Privacy-Safe**: Uses k-anonymity model - your actual password never leaves your computer
- **Password Strength Analysis**: Evaluates password complexity and provides improvement suggestions
- **Interactive Mode**: Secure hidden input for password checking
- **Command Line Support**: Batch checking multiple passwords
- **No Data Storage**: No passwords or results are stored locally or remotely

## 🛡️ How It Works

1. **Hash Generation**: Your password is converted to a SHA-1 hash locally on your machine
2. **K-Anonymity**: Only the first 5 characters of the hash are sent to the API
3. **Secure Lookup**: The API returns all hash suffixes that match the first 5 characters
4. **Local Matching**: Your computer checks if your full hash matches any returned results
5. **Result Display**: Shows if password was found in breaches and provides security feedback

**Your actual password never leaves your computer!**

## 📋 Prerequisites

- **Python 3.6+** - [Download Python](https://python.org/downloads/)
- **Internet Connection** - Required to query the HaveIBeenPwned API
- **Command Line/Terminal Access** - Basic terminal knowledge helpful

## ⚡ Quick Start

### 1. Clone or Download

**Option A: Download Files**
- Download `password_checker.py` and save to your computer
- Download `interactive_password_checker.py` for the enhanced version

**Option B: Clone Repository**
```bash
git clone https://github.com/yourusername/password-security-checker.git
cd password-security-checker
```

### 2. Install Dependencies

```bash
pip install requests
```

### 3. Run the Script

**Interactive Mode (Recommended):**
```bash
python interactive_password_checker.py
```

**Command Line Mode:**
```bash
python password_checker.py "your_password_here"
```

## 🚀 Usage Examples

### Interactive Mode
```bash
$ python interactive_password_checker.py

🔐 Password Security Checker
========================================
This tool checks if your password has been found in data breaches.
Your password is never sent to the server - only a partial hash is used.

Press Ctrl+C to exit anytime

Enter password to check (hidden input): [password hidden]

🔍 Checking password security...

📊 RESULTS:
--------------------
❌ COMPROMISED: This password was found 2390282 times in data breaches!
🚨 You should change this password immediately!

💪 Password Strength: 1/5
🔴 Weak password structure

💡 Suggestions to improve:
   • Use at least 8 characters
   • Include uppercase letters
   • Include numbers
   • Include special characters

==================================================

Check another password? (y/n): 
```

### Command Line Mode
```bash
# Check single password
$ python password_checker.py "password123"
password123 was found 2390282 times... you should probably change your password!

# Check multiple passwords
$ python password_checker.py "password123" "MyStr0ngP@ssw0rd!" "qwerty"
password123 was found 2390282 times... you should probably change your password!
MyStr0ngP@ssw0rd! was NOT found. Carry on!
qwerty was found 3912816 times... you should probably change your password!
```

## 📊 Understanding Results

### Breach Check Results
- **✅ NOT FOUND**: Password not in known breaches (good!)
- **❌ FOUND X TIMES**: Password compromised in breaches (change immediately!)

### Password Strength Score (0-5)
- **🟢 4-5 Points**: Strong password structure
- **🟡 2-3 Points**: Moderate password structure  
- **🔴 0-1 Points**: Weak password structure

### Strength Criteria
1. **Length**: At least 8 characters
2. **Lowercase**: Contains lowercase letters (a-z)
3. **Uppercase**: Contains uppercase letters (A-Z)
4. **Numbers**: Contains digits (0-9)
5. **Special Characters**: Contains symbols (!@#$%^&* etc.)

## 🔒 Security & Privacy

### Why This Tool is Safe
- **No Password Transmission**: Your actual password never leaves your device
- **K-Anonymity Model**: Only partial hash data is sent to the API
- **Trusted Source**: Uses HaveIBeenPwned, a service trusted by security professionals worldwide
- **Open Source**: Code is transparent and auditable
- **No Logging**: No passwords or results are stored anywhere

### Privacy Protection
```
Your Password: "MyPassword123"
SHA-1 Hash: "A94A8FE5CCB19BA61C4C0873D391E987982FBBD3"
Sent to API: "A94A8" (first 5 characters only)
API Returns: All hashes starting with "A94A8"
Local Check: Finds if full hash exists in returned list
```

## 🧪 Testing the Tool

### Safe Test Passwords (Known Compromised)
Try these common passwords to see the tool in action:
- `password123` - Very common
- `qwerty` - Keyboard pattern
- `123456` - Simple sequence
- `password` - Too simple

### Good Password Examples
These should show as NOT FOUND:
- `Tr0ub4dor&3` - Complex with mixed case, numbers, symbols
- `MyDog$Name2024!` - Personal but complex
- `Coffee#Lover789` - Memorable but secure

## 📁 Project Structure

```
password-security-checker/
├── README.md
├── password_checker.py          # Original command-line version
├── interactive_password_checker.py  # Enhanced interactive version
├── requirements.txt             # Python dependencies
└── examples/
    ├── basic_usage.py          # Usage examples
    └── test_passwords.txt      # Sample passwords for testing
```

## 🔧 Configuration

### Environment Variables (Optional)
```bash
# Set custom API timeout (default: 10 seconds)
export PWNED_API_TIMEOUT=15

# Enable debug mode
export PWNED_DEBUG=true
```

### Customization Options
You can modify the script to:
- Change password strength criteria
- Add additional security checks
- Integrate with password managers
- Create batch processing scripts

## 🚨 Important Security Notes

### DO NOT:
- ❌ Check passwords you're currently using on important accounts
- ❌ Use this on public or shared computers
- ❌ Share your results with others
- ❌ Test other people's passwords without permission

### DO:
- ✅ Use this to evaluate potential new passwords
- ✅ Run this on your personal, secure computer
- ✅ Change any passwords that show up as compromised
- ✅ Use strong, unique passwords for each account

## 🆘 Troubleshooting

### Common Issues

**"Module 'requests' not found"**
```bash
pip install requests
```

**"Error fetching: 429"**
- API rate limit reached, wait a few minutes and try again

**"Error fetching: 503"**
- HaveIBeenPwned service temporarily unavailable, try again later

**"Permission denied"**
- Make sure you have permission to run Python scripts in your directory

### Getting Help
1. Check the error message