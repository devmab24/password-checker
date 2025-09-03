#!/usr/bin/env python3
"""
Batch Password Checker

This script demonstrates how to check multiple passwords from a file
or list, useful for security audits or password policy enforcement.
"""

import sys
import os
import csv
import time
from datetime import datetime

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from password_checker import pwned_api_check

class BatchPasswordChecker:
    def __init__(self, delay=0.5):
        """
        Initialize batch checker with API rate limiting
        
        Args:
            delay (float): Delay between API calls to respect rate limits
        """
        self.delay = delay
        self.results = []
    
    def check_passwords_from_list(self, passwords, show_progress=True):
        """
        Check a list of passwords for breaches
        
        Args:
            passwords (list): List of passwords to check
            show_progress (bool): Whether to show progress updates
            
        Returns:
            list: Results with password status and breach counts
        """
        results = []
        total = len(passwords)
        
        if show_progress:
            print(f"🔍 Checking {total} passwords...")
            print("-" * 40)
        
        for i, password in enumerate(passwords, 1):
            if show_progress and i % 10 == 0:
                print(f"Progress: {i}/{total} passwords checked...")
            
            try:
                breach_count = pwned_api_check(password)
                status = "COMPROMISED" if breach_count else "SAFE"
                
                result = {
                    'password': password,
                    'status': status,
                    'breach_count': breach_count,
                    'checked_at': datetime.now().isoformat()
                }
                results.append(result)
                
                if show_progress:
                    emoji = "❌" if breach_count else "✅"
                    count_text = f"({breach_count} times)" if breach_count else ""
                    print(f"{emoji} Password {i}: {status} {count_text}")
                
                # Rate limiting
                if self.delay > 0:
                    time.sleep(self.delay)
                    
            except Exception as e:
                result = {
                    'password': password,
                    'status': 'ERROR',
                    'breach_count': None,
                    'error': str(e),
                    'checked_at': datetime.now().isoformat()
                }
                results.append(result)
                
                if show_progress:
                    print(f"❌ Password {i}: ERROR - {e}")
        
        return results
    
    def check_passwords_from_file(self, filename):
        """
        Read passwords from a text file and check them
        
        Args:
            filename (str): Path to file containing passwords (one per line)
            
        Returns:
            list: Results with password status and breach counts
        """
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                passwords = [line.strip() for line in f if line.strip()]
            
            print(f"📁 Loaded {len(passwords)} passwords from {filename}")
            return self.check_passwords_from_list(passwords)
            
        except FileNotFoundError:
            print(f"❌ Error: File '{filename}' not found")
            return []
        except Exception as e:
            print(f"❌ Error reading file: {e}")
            return []
    
    def generate_report(self, results, output_file=None):
        """
        Generate a summary report of the password check results
        
        Args:
            results (list): Results from password checking
            output_file (str): Optional file to save the report
        """
        if not results:
            print("No results to report")
            return
        
        # Calculate statistics
        total = len(results)
        compromised = sum(1 for r in results if r['status'] == 'COMPROMISED')
        safe = sum(1 for r in results if r['status'] == 'SAFE')
        errors = sum(1 for r in results if r['status'] == 'ERROR')
        
        # Find most compromised passwords
        compromised_results = [r for r in results if r['status'] == 'COMPROMISED']
        if compromised_results:
            most_compromised = max(compromised_results, key=lambda x: x['breach_count'])
        else:
            most_compromised = None
        
        # Generate report
        report = []
        report.append("🔐 BATCH PASSWORD SECURITY REPORT")
        report.append("=" * 50)
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")
        
        report.append("📊 SUMMARY STATISTICS")
        report.append("-" * 30)
        report.append(f"Total Passwords Checked: {total}")
        report.append(f"✅ Safe Passwords: {safe} ({safe/total*100:.1f}%)")
        report.append(f"❌ Compromised Passwords: {compromised} ({compromised/total*100:.1f}%)")
        report.append(f"⚠️  Errors: {errors} ({errors/total*100:.1f}%)")
        report.append("")
        
        if most_compromised:
            report.append("🚨 MOST COMPROMISED PASSWORD")
            report.append("-" * 30)
            report.append(f"Password: {most_compromised['password']}")
            report.append(f"Found in breaches: {most_compromised['breach_count']:,} times")
            report.append("")
        
        # Top 10 most compromised passwords
        if compromised_results:
            top_compromised = sorted(compromised_results, 
                                   key=lambda x: x['breach_count'], 
                                   reverse=True)[:10]
            
            report.append("🔝 TOP 10 MOST COMPROMISED PASSWORDS")
            report.append("-" * 40)
            for i, result in enumerate(top_compromised, 1):
                report.append(f"{i:2d}. {result['password']} ({result['breach_count']:,} times)")
            report.append("")
        
        # Recommendations
        report.append("💡 RECOMMENDATIONS")
        report.append("-" * 20)
        if compromised > 0:
            report.append("🔴 URGENT: Change all compromised passwords immediately")
            report.append("🔸 Use unique passwords for each account")
            report.append("🔸 Consider using a password manager")
            report.append("🔸 Enable two-factor authentication where possible")
        else:
            report.append("🟢 Great! No compromised passwords found")
            report.append("🔸 Continue using strong, unique passwords")
            report.append("🔸 Regular security checkups are recommended")
        
        # Print report
        report_text = '\n'.join(report)
        print(report_text)
        
        # Save to file if requested
        if output_file:
            try:
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(report_text)
                print(f"\n📄 Report saved to: {output_file}")
            except Exception as e:
                print(f"❌ Error saving report: {e}")
    
    def export_to_csv(self, results, filename):
        """
        Export results to CSV file
        
        Args:
            results (list): Results from password checking
            filename (str): CSV filename to create
        """
        if not results:
            print("No results to export")
            return
        
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                fieldnames = ['password', 'status', 'breach_count', 'checked_at']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                
                writer.writeheader()
                for result in results:
                    # Only include fields that exist in the result
                    row = {k: v for k, v in result.items() if k in fieldnames}
                    writer.writerow(row)
            
            print(f"📊 Results exported to: {filename}")
            
        except Exception as e:
            print(f"❌ Error exporting to CSV: {e}")

def main():
    """Demo the batch password checker"""
    print("🔐 Batch Password Checker Demo")
    print("=" * 40)
    
    # Example password list (mix of safe and compromised)
    demo_passwords = [
        "password123",      # Very compromised
        "admin",            # Very compromised
        "MyStr0ng!P@ssw0rd2024",  # Should be safe
        "qwerty",           # Compromised
        "letmein",          # Compromised
        "Tr0ub4dor&3",      # Likely safe
        "123456",           # Very compromised
        "welcome123",       # Likely compromised
    ]
    
    # Initialize batch checker
    checker = BatchPasswordChecker(delay=0.3)  # Small delay to be nice to API
    
    # Run batch check
    print(f"Testing with {len(demo_passwords)} demo passwords...")
    results = checker.check_passwords_from_list(demo_passwords)
    
    # Generate report
    print("\n" + "="*50)
    checker.generate_report(results)
    
    # Demonstrate CSV export
    csv_filename = f"password_check_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    checker.export_to_csv(results, csv_filename)
    
    print("\n💡 To check passwords from a file:")
    print("   checker.check_passwords_from_file('passwords.txt')")
    print("\n💡 To save report to file:")
    print("   checker.generate_report(results, 'security_report.txt')")

if __name__ == "__main__":
    main()