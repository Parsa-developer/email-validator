📧 Email Validator 🔍
Welcome to the Email Validator, a sleek Python tool to verify email addresses! 🧪 This command-line application checks if an email has valid syntax and optionally verifies the domain's mail server using DNS lookup. Perfect for ensuring your email lists are legit! 🚀

🌟 Features

✅ Validates email syntax using a robust regular expression.
🌐 Optional domain validation via MX record DNS lookup.
🖥️ User-friendly command-line interface with clear feedback.
🔄 Supports checking multiple emails in one session.
😊 Emoji-enhanced output for a fun experience.


🛠️ Requirements

Python 3.x 🐍
dnspython library for domain validation (pip install dnspython)


📦 Installation

Clone this repository:git clone https://github.com/parsa-developer/email-validator.git


Navigate to the project directory:cd email-validator


Install the required library:pip install dnspython




🎯 Usage

Run the script:python email_validator.py


Enter an email address to validate. 📩
Choose whether to check the domain's mail server (requires internet connection).
Get instant feedback on whether the email is valid. ✅ or ❌
Check more emails or exit when done.


📸 Example
Welcome to the Email Validator! 📧
Enter an email address to check its validity.

Enter email address (or 'exit' to quit): example@gmail.com
Check domain validity (yes/no)? yes
✅ Email is valid (syntax and domain checked).

Check another email? (yes/no): yes

Enter email address (or 'exit' to quit): invalid@fake.domain
Check domain validity (yes/no)? yes
❌ Invalid domain or no mail server found.

Check another email? (yes/no): no
Goodbye! 🚀


🔧 Notes

Syntax Check: Validates email format (e.g., user@domain.com) using regex.
Domain Check: Verifies if the domain has a mail server (MX records). Requires dnspython and an internet connection.
Limitations: Domain checks may fail for new or obscure domains due to DNS issues. Syntax check is always performed first.
Exit: Type exit at any time to quit.


🚀 Future Improvements

🎨 Add a GUI with tkinter or PyQt for a visual interface.
📋 Support batch validation from a file (e.g., CSV or TXT).
🔎 Enhance domain checks with SMTP verification.
📊 Generate reports for multiple email validations.
🛡️ Add more robust regex patterns for edge cases.


🤝 Contributing
Got ideas to make this validator even better? 🌈 Fork the repo, submit pull requests, or open issues for bugs or feature suggestions. Let’s ensure every email is valid! 💪

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

Validate emails like a pro! 📧 Give this repo a ⭐ if it helps you clean your email lists!
