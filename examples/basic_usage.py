#!/usr/bin/env python3
"""
Basic Usage Examples for Password Checker

This file demonstrates various ways to use the password checker functions
in your own scripts or applications.
"""

import sys
import os

# Add parent directory to path to import password checker modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from password_checker import pwned_api_check

def example_single_password_check():
    """Example 1: Check a single password"""
    print("Example 1: Checking a single password")
    print("-" * 40)
    
    password = "password123"  # Known compromised password for demo
    try:
        count = pwned_api_check(password)
        if count:
            print(f"❌ '{password}' found {count} times in breaches")
        else:
            print(f"✅ '{password}' not found in breaches")
    except Exception as e:
        print(f"Error: {e}")
    print()

def example_multiple_passwords():
    """Example 2: Check multiple passwords"""
    print("Example 2: Checking multiple passwords")
    print("-" * 40)
    
    # Mix of compromised and potentially secure passwords
    test_passwords = [
        "password123",      # Very common - will be compromised
        "qwerty",          # Common keyboard pattern - compromised
        "Tr0ub4dor&3",     # Strong password - likely not compromised
        "123456",          # Very simple - compromised
    ]
    
    for password in test_passwords:
        try:
            count = pwned_api_check(password)
            status = "❌ COMPROMISED" if count else "✅ SAFE"
            times = f"({count} times)" if count else ""
            print(f"{status} '{password}' {times}")
        except Exception as e:
            print(f"❌ ERROR checking '{password}': {e}")
    print()

def example_password_validation_function():
    """Example 3: Create a password validation function"""
    print("Example 3: Password validation function")
    print("-" * 40)
    
    def validate_password(password, min_length=8):
        """
        Comprehensive password validation function
        Returns: (is_valid, issues, breach_count)
        """
        issues = []
        
        # Length check
        if len(password) < min_length:
            issues.append(f"Password must be at least {min_length} characters long")
        
        # Character variety checks
        if not any(c.islower() for c in password):
            issues.append("Password must contain lowercase letters")
        if not any(c.isupper() for c in password):
            issues.append("Password must contain uppercase letters")
        if not any(c.isdigit() for c in password):
            issues.append("Password must contain numbers")
        if not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
            issues.append("Password must contain special characters")
        
        # Breach check
        try:
            breach_count = pwned_api_check(password)
            if breach_count:
                issues.append(f"Password found in {breach_count} data breaches")
        except Exception as e:
            breach_count = None
            issues.append(f"Could not check breaches: {e}")
        
        is_valid = len(issues) == 0
        return is_valid, issues, breach_count
    
    # Test the validation function
    test_password = "MySecureP@ssw0rd2024"
    is_valid, issues, breach_count = validate_password(test_password)
    
    print(f"Testing password: '{test_password}'")
    print(f"Valid: {is_valid}")
    if issues:
        print("Issues found:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("✅ Password meets all criteria!")
    print()

def example_batch_password_file():
    """Example 4: Check passwords from a file"""
    print("Example 4: Batch checking from file")
    print("-" * 40)
    
    # This would typically read from a file, but we'll use a list for demo
    passwords_from_file = [
        "admin",
        "welcome123",
        "MyStr0ng!P@ssw0rd",
        "letmein"
    ]
    
    print("Checking passwords from batch list...")
    compromised_count = 0
    safe_count = 0
    
    for i, password in enumerate(passwords_from_file, 1):
        try:
            breach_count = pwned_api_check(password)
            if breach_count:
                print(f"{i}. ❌ Password {i} compromised ({breach_count} times)")
                compromised_count += 1
            else:
                print(f"{i}. ✅ Password {i} appears safe")
                safe_count += 1
        except Exception as e:
            print(f"{i}. ❌ Error checking password {i}: {e}")
    
    print(f"\nSummary: {safe_count} safe, {compromised_count} compromised")
    print()

def example_integration_with_user_registration():
    """Example 5: Integration example for user registration"""
    print("Example 5: User registration integration")
    print("-" * 40)
    
    def register_user_password(username, password):
        """
        Example function for user registration with password checking
        """
        print(f"Registering user: {username}")
        
        # Basic validations
        if len(password) < 8:
            return False, "Password must be at least 8 characters long"
        
        # Check if password is compromised
        try:
            breach_count = pwned_api_check(password)
            if breach_count:
                if breach_count > 100000:  # Very common password
                    return False, f"This password is too common (found {breach_count} times in breaches). Please choose a different password."
                elif breach_count > 1000:  # Somewhat common
                    return False, f"This password has been compromised {breach_count} times. Please choose a different password."
                else:  # Found but not very common
                    print(f"⚠️  Warning: This password was found {breach_count} times in breaches, but proceeding with registration.")
            
            return True, "Password accepted"
            
        except Exception as e:
            print(f"⚠️  Could not verify password security: {e}")
            return True, "Password accepted (security check unavailable)"
    
    # Test the registration function
    test_cases = [
        ("user1", "password123"),  # Very compromised
        ("user2", "MyStr0ng!P@ssw0rd2024"),  # Should be safe
        ("user3", "short"),  # Too short
    ]
    
    for username, password in test_cases:
        success, message = register_user_password(username, password)
        status = "✅ SUCCESS" if success else "❌ REJECTED"
        print(f"{status}: {username} - {message}")
    print()

def main():
    """Run all examples"""
    print("🔐 Password Checker - Usage Examples")
    print("=" * 50)
    print()
    
    try:
        example_single_password_check()
        example_multiple_passwords()
        example_password_validation_function()
        example_batch_password_file()
        example_integration_with_user_registration()
        
        print("✅ All examples completed successfully!")
        print("\n💡 Note: Some passwords used in examples are intentionally")
        print("   weak or compromised to demonstrate the tool's functionality.")
        
    except Exception as e:
        print(f"❌ Error running examples: {e}")
        print("Make sure you have the 'requests' module installed:")
        print("pip install requests")

if __name__ == "__main__":
    main()