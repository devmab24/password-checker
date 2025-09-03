#You can run this file here using the terminal. 
#You will also need to make sure you have installed the requests module from PyPi (pip install)

import requests
import hashlib
import sys
import getpass

def request_api_data(query_char):
    """Request data from HaveIBeenPwned API"""
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    """Parse API response to find password hash matches"""
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    """Check if password exists in breached databases"""
    # Create SHA1 hash of password
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # Split hash: send only first 5 chars to API (k-anonymity)
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)

def check_password_strength(password):
    """Basic password strength indicators"""
    strength_score = 0
    feedback = []
    
    if len(password) >= 8:
        strength_score += 1
    else:
        feedback.append("Use at least 8 characters")
    
    if any(c.islower() for c in password):
        strength_score += 1
    else:
        feedback.append("Include lowercase letters")
    
    if any(c.isupper() for c in password):
        strength_score += 1
    else:
        feedback.append("Include uppercase letters")
    
    if any(c.isdigit() for c in password):
        strength_score += 1
    else:
        feedback.append("Include numbers")
    
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        strength_score += 1
    else:
        feedback.append("Include special characters")
    
    return strength_score, feedback

def main():
    print("🔐 Password Security Checker")
    print("=" * 40)
    print("This tool checks if your password has been found in data breaches.")
    print("Your password is never sent to the server - only a partial hash is used.")
    print("\nPress Ctrl+C to exit anytime\n")
    
    try:
        while True:
            # Use getpass for secure password input (doesn't show on screen)
            password = getpass.getpass("Enter password to check (hidden input): ")
            
            if not password:
                print("❌ Please enter a password\n")
                continue
            
            print("\n🔍 Checking password security...")
            
            try:
                # Check against breached databases
                count = pwned_api_check(password)
                
                # Check basic password strength
                strength_score, feedback = check_password_strength(password)
                
                print("\n📊 RESULTS:")
                print("-" * 20)
                
                # Breach check results
                if count:
                    print(f"❌ COMPROMISED: This password was found {count} times in data breaches!")
                    print("🚨 You should change this password immediately!")
                else:
                    print("✅ GOOD: This password was not found in known data breaches.")
                
                # Strength assessment
                print(f"\n💪 Password Strength: {strength_score}/5")
                if strength_score >= 4:
                    print("🟢 Strong password structure")
                elif strength_score >= 3:
                    print("🟡 Moderate password structure")
                else:
                    print("🔴 Weak password structure")
                
                if feedback:
                    print("\n💡 Suggestions to improve:")
                    for tip in feedback:
                        print(f"   • {tip}")
                
                print("\n" + "="*50)
                
                # Ask if user wants to check another password
                again = input("\nCheck another password? (y/n): ").lower().strip()
                if again not in ['y', 'yes']:
                    break
                    
            except RuntimeError as e:
                print(f"❌ Error: {e}")
                print("Please check your internet connection and try again.")
            except Exception as e:
                print(f"❌ Unexpected error: {e}")
    
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye! Stay secure!")
    
    return "Password checking completed!"

if __name__ == '__main__':
    main()
