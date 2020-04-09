import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

address_book = ['nontachai.yoo@pea.co.th', 'pornchai.cha@pea.co.th']
import smtplib, ssl

port = 465  # For starttls
smtp_server = "email.pea.co.th"
sender_email = "nontachai.yoo@pea.co.th"
receiver_email = "pornchai.cha@pea.co.th"
password = 'PEAadmin1oo%'
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL("mailspro.pea.co.th", port, context=context) as server:
    server.login("nontachai.yoo@pea.co.th", password)
    server.sendmail(sender_email, receiver_email, message)