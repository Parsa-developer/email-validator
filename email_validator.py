import socket
import re
import dns.resolver

def is_valid_email_syntax(email):
    email_pattern = r'^[a-zA-Z0-9._+%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_pattern, email))

def is_valid_domain(email):
    try:
        domain = email.split('@')[1]
        dns.resolver.resolve(domain, 'MX')
        return True
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.NoNameservers, dns.resolver.Timeout):
        return False
    except Exception as e:
        print(f"Error checking domain: {e}")
        return False
    
def validate_email(email, check_domain=False):
    if not is_valid_email_syntax(email):
        return False, "Invalid email syntax. Ensure it follows the format: user@domain.com"
    
    if check_domain:
        if not is_valid_domain(email):
            return False, "Invalid domain or no mail server found."
        return True, "Email is valid (syntax and domain checked)."
    return True, "Email syntax is valid."

def main():
    print("Welcome to the Email Validator! 📧")
    print("Enter an email address to check its validity.")

    while True:
        email = input("Please enter your email address: (or exit to quit) ").strip()
        if email.lower() == "exit":
            print("Thanks for using the Email Validator! 😊")
            break
        check_domain = input("Check domain validity (yes/no)? ").lower() == "yes"
        is_valid, message = validate_email(email, check_domain)

        if is_valid:
            print(f"✅ {message}")
        else:
            print(f"❌ {message}")
        
        continue_check = input("\nCheck another email? (yes/no): ").lower()
        if continue_check != 'yes':
            print("Goodbye! 🚀")
            break

if __name__ == "__main__":
    main()