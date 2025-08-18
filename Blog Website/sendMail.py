import smtplib, os
from dotenv import load_dotenv

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
TO_ADDRS = os.getenv("TO_ADDRS")

class MailBot:
    def __init__(self, name, email, phone_number, message):
        load_dotenv()


        with smtplib.SMTP("smtp.gmail.com") as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, TO_ADDRS, f"Subject: New Message \n\nName: {name}\nEmail: {email}\nPhone: {phone_number}\nMessage: {message}")