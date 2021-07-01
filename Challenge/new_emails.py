#!/usr/bin/env python3

from email.message import EmailMessage
import os
import mimetypes
import smtplib

def generate_email():
    message = EmailMessage()
    message["From"] = "automation@example.com"
    message["To"] = input("recipient:\n")
    message["Subject"] = input("subject:\n")
    message.set_content(input("content:\n"))
    attachment_path = input("path to attachment:\n")
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split("/", 1)
    with open(attachment_path, "rb") as ap:
        message.add_attachment(ap.read(),
                maintype=mime_type,
                subtype=mime_subtype,
                filename=os.path.basename(attachment_path))
    return message

def send_email(message):
    mail_server = smtplib.SMTP('localhost', 1025)
    mail_server.send_message(message)
    mail_server.quit()

send_email(generate_email())
