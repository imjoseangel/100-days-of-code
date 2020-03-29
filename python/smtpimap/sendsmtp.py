#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
import smtplib
import socket

SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USER = ''
SMTP_PASS = ''

# Craft the email by hand
from_email = SMTP_USER  # or simply the email address
to_emails = [SMTP_USER]
body = "Hello, world!"
headers = f"From: {from_email}\r\n"
headers += f"To: {', '.join(to_emails)}\r\n"
headers += f"Subject: Hello\r\n"
email_message = headers + "\r\n" + body  # Blank line needed between headers and body


def main():
    try:
        smtp_server = smtplib.SMTP(SMTP_HOST, port=SMTP_PORT)
        smtp_server.set_debuglevel(1)  # Show SMTP server interactions
        smtp_server.ehlo()
        smtp_server.starttls()
        print("Connection successful")
        smtp_server.login(SMTP_USER, SMTP_PASS)
        smtp_server.sendmail(from_email, to_emails, email_message)
        # ...send emails
    except socket.error as e:
        print("Something went wrong...\n Error message: {0}".format(e))


if __name__ == '__main__':
    main()
