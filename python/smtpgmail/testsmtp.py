#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
import smtplib
import socket


def main():
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        print("Connection successful")
        # ...send emails
    except socket.error as e:
        print("Something went wrong...\n Error message: {0}".format(e))


if __name__ == '__main__':
    main()
