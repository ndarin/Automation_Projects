#!/usr/bin/env python3

from email.message import EmailMessage
import smtplib
import getpass
import os
import mimetypes
#Defining the email labels
message = EmailMessage()
sender = 'tendaimoyo17@gmail.com'
recipient = 'lewismumoyo17@gmail.com'
body = """Hi.

I'm learning how to send an email using Python.
How cool is that?"""
#Setting the email keys and labels values
message['From'] = sender
message['To'] = recipient
message['Subject'] = "Greetings from {} to {}".format(sender, recipient)
message.set_content(body)

#Defining attachment variables
attachment_path = 'C:/Users/tawan/images/africa.jpg'
attachment_filename = os.path.basename(attachment_path)
mime_type, _ = mimetypes.guess_type(attachment_path)
mime_main, mime_subtype = mime_type.split('/', 1)

#Adding the email attachment
with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
                            maintype=mime_main,
                            subtype=mime_subtype,
                            filename=os.path.basename(attachment_path))

#Seting up mail server connection
mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
mail_server.set_debuglevel(1)
mail_pass = getpass.getpass('Password? ')
mail_server.login(sender, mail_pass)

#Sending the email
mail_server.send_message(message)
#Close the connection
mail_server.quit()
