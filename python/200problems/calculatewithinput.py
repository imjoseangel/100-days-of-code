#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

# Write a Python program that accepts an integer (n)
# and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5

loop = True
while loop:
    integer = int(input("Input Integer between 1 and 9: "))
    if 0 < integer < 10:
        loop = False

print(integer + int(2 * str(integer)) + int(3 * str(integer)))
