#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Interactive Dictionary in Python"""

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
#Import libraries
import time
from datetime import datetime as dt

#Path to the host file, redirect to local host, list of websits to block
HOST_PATH = "hosts"
REDIRECT = "127.0.0.1"
WEBSITE_LIST = ["www.google.com", "www.facebook.com"]

while True:
    #Check for the current time
    if dt(dt.now().year,
          dt.now().month,
          dt.now().day, 8) < dt.now() < dt(dt.now().year,
                                           dt.now().month,
                                           dt.now().day, 16):
        print("Time to Work")

        #Open file and read the content
        FILE = open(HOST_PATH, "r+")
        CONTENT = FILE.read()
        for website in WEBSITE_LIST:
            if website in CONTENT:
                pass
            else:
                #Write the IP of loalhost and name of the website to block
                FILE.write(REDIRECT + " " + website + "\n")

    else:
        print("Fun Time")
        #Open hosts file and read content from it- line by line

        FILE = open(HOST_PATH, 'r+')
        CONTENT = FILE.readlines()
        #Take back pointer to starting of the file from the end of file
        FILE.seek(0)
        for line in CONTENT:
            if not any(website in line for website in WEBSITE_LIST):
                FILE.write(line)
            FILE.truncate()

    time.sleep(5)
