# Email Library
- Simple Mail Transfer Protocol (SMTP)
- Multipurpose Internet Mail Extensions (MIME)

```
>>> from email.message import EmailMessage
>>> message = EmailMessage()
>>> print(message) #empty
>>> sender = "me@example.com"
>>> recipient = "you@example.com"
#assining a sender and reciever to message
>>> message['From'] = sender
>>> message['To'] = recipient
>>> print(message)
From: me@example.com
To: you@example.com

>>> message["Subject"] = f'Greetings from {sender} to {recipient}"
>>> print(message)
From: me@example.com
To: you@example.com
Subject: Greetings from me@example.com to you@example.com

>>> body = """
Hey there!
im learning to send emails using python!
"""

>>> message.set_content(body)

```

## Adding Attachments
```
>>> import os
>>> import mimetypes
>>> attachment_path = "/tmp/example.png"
>>> attachment_filename = os.path.basename(attachment_path)
>>> mime_type, _ = mimetypes.guess_type(attachment_path)
>>> print(mime_type)
image/png #mimetype and subtype seperated by a /
```

```
>>> with open(attachment_path, 'rb') as ap:
...     message.add_attachment(ap.read(),
...                            maintype=mime_type,
...                            subtype=mime_subtype,
...                            filename=os.path.basename(attachment_path))
... 
>>> print(message)
Content-Type: multipart/mixed; boundary="===============5350123048127315795=="

--===============5350123048127315795==
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: 7bit

Hey there!

I'm learning to send email using Python!

--===============5350123048127315795==
Content-Type: image/png
Content-Transfer-Encoding: base64
Content-Disposition: attachment; filename="example.png"
MIME-Version: 1.0

iVBORw0KGgoAAAANSUhEUgAAASIAAABSCAYAAADw69nDAAAACXBIWXMAAAsTAAALEwEAmpwYAAAg
AElEQVR4nO2dd3wUZf7HP8/M9k2nKIJA4BCUNJKgNJWIBUUgEggCiSgeVhA8jzv05Gc5z4KHiqin
eBZIIBDKIXggKIeCRCAhjQAqx4UiCARSt83uzDy/PzazTDZbwy4BnHde+9qZydNn97Pf5/uUIZRS
(...We deleted a bunch of lines here...)
wgAAAABJRU5ErkJggg==

--===============5350123048127315795==--
```
## Sending Email through an SMTP Server
```
import smtplib
```

create mail server object

```
>>> mail_server = smtplib.SMTP_SSL("smtp.example.com")
>>> mail_server.set_debuglevel(1)
```

set password
```
>>> mail_server.login(sender, password)
```

sending the email with the mail_server

```
>>> mail_server.send_message(message) # this method returns a dictionary of any recipients who were NOT able to recieve the message
```

close the mail server

```
>>> mail_server.quit()
```
