# #!/usr/bin/env python3
# """
# Integration Examples for Password Checker

# This file shows how to integrate the password checker into various
# real-world scenarios like web applications, CLI tools, and security audits.
# """

# import sys
# import os
# import json
# from datetime import datetime, timedelta

# # Add parent directory to path
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# from password_checker import pwned_api_check

# class PasswordPolicy:
#     """Example password policy enforcement with breach checking"""
    
#     def __init__(self, min_length=8, require_upper=True, require_lower=True, 
#                  require_digit=True, require_special=True, check_breaches=True):
#         self.min_length = min_length
#         self.require_upper = require_upper
#         self.require_lower = require_lower
#         self.require_digit = require_digit
#         self.require_special = require_special
#         self.check_breaches = check_breaches
#         self.special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
#     def validate_password(self, password):
#         """
#         Validate password against policy and breach database
        
#         Returns:
#             dict: Validation result with success status and details
#         """
#         result = {
#             'valid': True,
#             'errors': [],
#             'warnings': [],
#             'breach_count': None,
#             'strength_score': 0
#         }
        
#         # Length check
#         if len(password) < self.min_length:
#             result['errors'].append(f"Password must be at least {self.min_length} characters long")
#             result['valid'] = False
#         else:
#             result['strength_score'] += 1
        
#         # Character requirements
#         if self.require_upper and not any(c.isupper() for c in password):
#             result['errors'].append("Password must contain at least one uppercase letter")
#             result['valid'] = False
#         else:
#             result['strength_score'] += 1
            
#         if self.require_lower and not any(c.islower() for c in password):
#             result['errors'].append("Password must contain at least one lowercase letter")
#             result['valid'] = False
#         else:
#             result['strength_score'] += 1
            
#         if self.require_digit and not any(c.isdigit() for c in password):
#             result['errors'].append("Password must contain at least one digit")
#             result['valid'] = False
#         else:
#             result['strength_score'] += 1
            
#         if self.require_special and not any(c in self.special_chars for c in password):
#             result['errors'].append("Password must contain at least one special character")
#             result['valid'] = False
#         else:
#             result['strength_score'] += 1
        
#         # Breach check
#         if self.check_breaches and result['valid']:  # Only check if other criteria pass
#             try:
#                 breach_count = pwned_api_check(password)
#                 result['breach_count'] = breach_count
                
#                 if breach_count:
#                     if breach_count > 100000:
#                         result['errors'].append(f"Password is extremely common (found {breach_count:,} times in breaches)")
#                         result['valid'] = False
#                     elif breach_count > 10000:
#                         result['errors'].append(f"Password is very common (found {breach_count:,} times in breaches)")
#                         result['valid'] = False
#                     elif breach_count > 1000:
#                         result['warnings'].append(f"Password found {breach_count:,} times in breaches - consider changing")
#                     else:
#                         result['warnings'].append(f"Password found {breach_count} times in breaches")
                        
#             except Exception as e:
#                 result['warnings'].append(f"Could not check breach database: {e}")
        
#         return result

# class UserRegistrationExample:
#     """Example user registration system with password checking"""
    
#     def __init__(self):
#         self.users = {}  # Simple in-memory user store
#         self.password_policy = PasswordPolicy()
    
#     def register_user(self, username, password, email):
#         """
#         Register a new user with password validation
        
#         Returns:
#             dict: Registration result
#         """
#         result = {
#             'success': False,
#             'message': '',
#             'user_id': None,
#             'password_issues': []
#         }
        
#         # Check if user already exists
#         if username in self.users:
#             result['message'] = "Username already exists"
#             return result
        
#         # Validate password
#         password_validation = self.password_policy.validate_password(password)
        
#         if not password_validation['valid']:
#             result['message'] = "Password does not meet security requirements"
#             result['password_issues'] = password_validation['errors']
#             return result
        
#         # Create user
#         user_id = f"user_{len(self.users) + 1}"
#         self.users[username] = {
#             'user_id': user_id,
#             'username': username,
#             'email': email,
#             'created_at': datetime.now().isoformat(),
#             'password_strength': password_validation['strength_score'],
#             'breach_warnings': password_validation['warnings']
#         }
        
#         result.update({
#             'success': True,
#             'message': 'User registered successfully',
#             'user_id': user_id,
#             'password_warnings': password_validation['warnings']
#         })
        
#         return result

# class SecurityAuditTool:
#     """Example security audit tool for organizations"""
    
#     def __init__(self):
#         self.audit_results = []
    
#     def audit_user_passwords(self, users_passwords):
#         """
#         Audit a list of user passwords for security compliance
        
#         Args:
#             users_passwords (list): List of tuples (username, password)
            
#         Returns:
#             dict: Audit summary and detailed results
#         """
#         print("🔒 Starting Security Audit...")
#         print("-" * 40)
        
#         high_risk_users = []
#         medium_risk_users = []
#         compliant_users = []
        
#         for username, password in users_passwords:
#             print(f"Auditing user: {username}")
            
#             try:
#                 breach_count = pwned_api_check(password)
                
#                 risk_level = 'LOW'
#                 recommendations = []
                
#                 if breach_count:
#                     if breach_count > 50000:
#                         risk_level = 'CRITICAL'
#                         recommendations.append('IMMEDIATE password change required')
#                         high_risk_users.append(username)
#                     elif breach_count > 5000:
#                         risk_level = 'HIGH'
#                         recommendations.append('Password change strongly recommended')
#                         high_risk_users.append(username)
#                     elif breach_count > 100:
#                         risk_level = 'MEDIUM'
#                         recommendations.append('Consider password change')
#                         medium_risk_users.append(username)
#                     else:
#                         risk_level = 'LOW'
#                         recommendations.append('Monitor for future breaches')
#                         compliant_users.append(username)
#                 else:
#                     compliant_users.append(username)
#                     recommendations.append('Password appears secure')
                
#                 audit_entry = {
#                     'username': username,
#                     'risk_level': risk_level,
#                     'breach_count': breach_count,
#                     'recommendations': recommendations,
#                     'audit_date': datetime.now().isoformat()
#                 }
                
#                 self.audit_results.append(audit_entry)
                
#                 # Print immediate feedback
#                 risk_emoji = {'CRITICAL': '🔴', 'HIGH': '🟠', 'MEDIUM': '🟡', 'LOW': '🟢'}
#                 print(f"  {risk_emoji[risk_level]} {risk_level} risk - {breach_count or 0} breaches")
                
#             except Exception as e:
#                 print(f"  ❌ Error auditing {username}: {e}")
#                 audit_entry = {
#                     'username': username,
#                     'risk_level': 'UNKNOWN',
#                     'breach_count': None,
#                     'error': str(e),
#                     'audit_date': datetime.now().isoformat()
#                 }
#                 self.audit_results.append(audit_entry)
        
#         # Generate summary
#         summary = {
#             'total_users': len(users_passwords),
#             'high_risk_count': len(high_risk_users),
#             'medium_risk_count': len(medium_risk_users),
#             'compliant_count': len(compliant_users),
#             'high_risk_users': high_risk_users,
#             'medium_risk_users': medium_risk_users,
#             'compliance_rate': len(compliant_users) / len(users_passwords) * 100,
#             'audit_completed': datetime.now().isoformat()
#         }
        
#         return summary
    
#     def generate_audit_report(self, summary):
#         """Generate a formatted audit report"""
#         print("\n" + "="*50)
#         print("🔒 SECURITY AUDIT REPORT")
#         print("="*50)
#         print(f"Audit Date: {summary['audit_completed']}")
#         print(f"Total Users Audited: {summary['total_users']}")
#         print()
        
#         print("📊 RISK BREAKDOWN")
#         print("-" * 20)
#         print(f"🔴 High Risk Users: {summary['high_risk_count']}")
#         print(f"🟡 Medium Risk Users: {summary['medium_risk_count']}")
#         print(f"🟢 Compliant Users: {summary['compliant_count']}")
#         print(f"✅ Compliance Rate: {summary['compliance_rate']:.1f}%")
#         print()
        
#         if summary['high_risk_users']:
#             print("🚨 IMMEDIATE ACTION REQUIRED")
#             print("-" * 30)
#             for user in summary['high_risk_users']:
#                 print(f"  • {user}")
#             print()
        
#         print("💡 RECOMMENDATIONS")
#         print("-" * 18)
#         print("  • Implement mandatory password changes for high-risk users")
#         print("  • Enable multi-factor authentication")
#         print("  • Provide security awareness training")
#         print("  • Regular password audits (quarterly)")

# # def demo_password_policy():
# #     """Demo the password policy enforcement"""
# #     print("1️⃣  PASSWORD POLICY DEMO")
# #     print("=" * 30)
    
# #     policy = PasswordPolicy()
# #     test_passwords = [
# #         "password",
# #         "Password1",    