#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import imaplib
import email

# Connect and login to IMAP mail server
username = ''
password = ''
mail_server = 'imap.gmail.com'

imap_server = imaplib.IMAP4_SSL(host=mail_server)
imap_server.login(username, password)

# Choose the mailbox (folder) to search
# Case sensitive!
imap_server.select('INBOX')  # Default is `INBOX`

# Find all emails in inbox
_, message_numbers_raw = imap_server.search(None, 'ALL')
for message_number in message_numbers_raw[0].split():
    _, msg = imap_server.fetch(message_number, '(RFC822)')

    # Parse the raw email message in to a convenient object
    message = email.message_from_bytes(msg[0][1])
    print('== Email message =====')
    # print(message)  # print FULL message
    print('== Email details =====')
    print(f'From: {message["from"]}')
    print(f'To: {message["to"]}')
    print(f'Cc: {message["cc"]}')
    print(f'Bcc: {message["bcc"]}')
    print(f'Urgency (1 highest 5 lowest): {message["x-priority"]}')
    print(f'Object type: {type(message)}')
    print(f'Content type: {message.get_content_type()}')
    print(f'Content disposition: {message.get_content_disposition()}')
    print(f'Multipart?: {message.is_multipart()}')
    # If the message is multipart, it basically has multiple emails inside
    # so you must extract each "submail" separately.
    if message.is_multipart():
        print('Multipart types:')
        for part in message.walk():
            print(f'- {part.get_content_type()}')
        multipart_payload = message.get_payload()
        for sub_message in multipart_payload:
            # The actual text/HTML email contents, or attachment data
            print(f'Payload\n{sub_message.get_payload()}')
    else:  # Not a multipart message, payload is simple string
        print(f'Payload\n{message.get_payload()}')
    # You could also use `message.iter_attachments()` to get attachments only
