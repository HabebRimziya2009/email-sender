import os

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email_to_client(name, email, phone, service, message):
    sender_email = os.getenv("EMAIL_USERNAME")
    app_password = os.getenv("APP_PW")
    client_email = "habeb.rizmi@gmail.com"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    subject = f"New Contact Form Submission from {name}"
    body = f"""
You’ve received a new response from the contact form:

Name: {name}
Email: {email}
Phone: {phone}
Service: {service}
Message:
{message}
"""

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = client_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(msg)
