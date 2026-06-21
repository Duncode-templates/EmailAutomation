import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Optional

class EmailAutomation:
    """
    Automates sending branded HTML emails with company info and custom assets.
    """

    def __init__(self, smtp_server: str = "smtp.gmail.com", port: int = 587):
        self.smtp_server = smtp_server
        self.port = port

    def generate_html_template(
        self, 
        company_name: str, 
        image_url: str, 
        body_content: str,
        primary_color: str = "#4F46E5"
    ) -> str:
        """
        Generates a structured, responsive HTML email template.
        """
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 0; background-color: #f4f4f7; color: #51545e; }}
                .email-wrapper {{ width: 100%; margin: 0; padding: 0; background-color: #f4f4f7; }}
                .email-content {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
                .email-masthead {{ padding: 25px 0; text-align: center; }}
                .email-masthead_name {{ font-size: 16px; font-weight: bold; color: #a8aaaf; text-decoration: none; text-shadow: 0 1px 0 white; }}
                .email-body {{ width: 100%; margin: 0; padding: 0; border-top: 1px solid #e8e5ef; border-bottom: 1px solid #e8e5ef; background-color: #ffffff; }}
                .email-body_inner {{ width: 570px; margin: 0 auto; padding: 45px; }}
                .header-image {{ width: 100%; max-height: 300px; object-fit: cover; border-radius: 8px; margin-bottom: 25px; }}
                .content-cell {{ padding: 35px; }}
                h1 {{ margin-top: 0; color: #333333; font-size: 22px; font-weight: bold; text-align: left; }}
                p {{ margin: .4em 0 1.1875em; font-size: 16px; line-height: 1.625; color: #51545e; }}
                .button {{ background-color: {primary_color}; border-top: 10px solid {primary_color}; border-right: 18px solid {primary_color}; border-bottom: 10px solid {primary_color}; border-left: 18px solid {primary_color}; display: inline-block; color: #FFF; text-decoration: none; border-radius: 3px; box-shadow: 0 2px 3px rgba(0, 0, 0, 0.16); -webkit-text-size-adjust: none; box-sizing: border-box; }}
                .email-footer {{ width: 570px; margin: 0 auto; padding: 35px; text-align: center; }}
                .email-footer p {{ font-size: 12px; color: #6b7280; }}
            </style>
        </head>
        <body>
            <div class="email-wrapper">
                <div class="email-content">
                    <div class="email-masthead">
                        <a href="#" class="email-masthead_name">{company_name}</a>
                    </div>
                    <div class="email-body">
                        <div class="email-body_inner">
                            <img src="{image_url}" alt="{company_name} Branding" class="header-image" />
                            <h1>Welcome to {company_name}</h1>
                            <div class="body-text">
                                {body_content}
                            </div>
                        </div>
                    </div>
                    <div class="email-footer">
                        <p>&copy; 2026 {company_name}. All rights reserved.</p>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """

    def send_email(
        self,
        sender_email: str,
        password: str,
        recipient_email: str,
        subject: str,
        html_content: str
    ):
        """
        Sends the HTML email using SMTP.
        Note: For Gmail, you usually need an 'App Password'.
        """
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = recipient_email

        # Attach HTML content
        part = MIMEText(html_content, "html")
        msg.attach(part)

        try:
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, recipient_email, msg.as_string())
            return {"status": "success", "message": f"Email sent to {recipient_email}"}
        except Exception as e:
            return {"status": "error", "message": str(e)}
