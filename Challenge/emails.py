#!/usr/bin/env python3

from email.message import EmailMessage
import os
import mimetypes
import smtplib

def generate_email():
    message = EmailMessage()
    message["From"] = "automation@example.com"
    message["To"] = "{}@example.com".format(os.environ.get('USER'))
    message["Subject"] = "Upload Completed - Online Fruit Store"
    message.set_content("All fruits are uploaded to our website successfully. A detailed list is attached to this email.")

    attachment_path = "/tmp/processed.pdf"
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split("/", 1)
    with open(attachment_path, "rb") as ap:
        message.add_attachment(ap.read(),
                maintype=mime_type,
                subtype=mime_subtype,
                filename=os.path.basename(attachment_path))
    return message

def send_email(message):
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()

