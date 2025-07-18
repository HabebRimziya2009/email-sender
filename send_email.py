import os

from flask import Flask, request
from flask_cors import CORS
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
CORS(app)


@app.route("/send", methods=["POST"])
def send_email():
    data = request.form
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    msg = EmailMessage()
    msg.set_content(f"Message from {name} ({email}):\n\n{message}")
    msg["Subject"] = "New Contact Form"
    msg["From"] = os.getenv("USERNAME")
    msg["To"] = email

    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp.login(os.getenv("USERNAME"), os.getenv("APP_PW"))
    smtp.send_message(msg)
    smtp.quit()

    return "Sent", 200
