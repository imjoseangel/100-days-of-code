#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import datetime

# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that
# they will turn 100 years old.

name = input("What is your name? ")
age = int(input("How old are you? "))
currentyear = int(str(datetime.date.today())[:4])

hundred = currentyear - age + 100

print(f"{ name } will be 100 years old in the year { hundred }")
