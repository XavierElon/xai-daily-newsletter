import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

def send_email(subject: str, body: str, to_email: str):
    """
    Send an email with the given subject and body to the given email address.
    """
    sender_email = os.getenv("EMAIL_SENDER")