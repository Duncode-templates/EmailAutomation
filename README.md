# Email Sender Automation

A Python package for automating branded, professional HTML emails.

## Features

- **Branded Templates**: Automatically generate responsive HTML emails with your company name and logo.
- **Custom Assets**: Easily include images and custom HTML/CSS content.
- **Gmail Ready**: Pre-configured for SMTP sending via Gmail.

## Installation

```bash
pip install .
```

## Usage

```python
from email_sender_automation import EmailAutomation

# 1. Initialize the automation
automation = EmailAutomation()

# 2. Generate a professional HTML template
html = automation.generate_html_template(
    company_name="Awesome Corp",
    image_url="https://example.com/logo.png",
    body_content="<p>We are excited to share some updates with you!</p>",
    primary_color="#2563EB"
)

# 3. Send the email
# Note: Use your Gmail 'App Password' for authentication
result = automation.send_email(
    sender_email="your-email@gmail.com",
    password="your-app-password",
    recipient_email="customer@example.com",
    subject="Welcome to Awesome Corp",
    html_content=html
)

print(result)
```
