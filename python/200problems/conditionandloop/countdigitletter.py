#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Write a Python program that accepts a string and
# calculate the number of digits and letters
# Sample Data : "Python 3.2"
# Expected Output :
# Letters 6
# Digits 2

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)


def countdigitletters(mytext):
    letters = 0
    digits = 0
    for item in mytext:
        if item.isalpha():
            letters += 1
        elif item.isdigit():
            digits += 1
    return letters, digits


def main():
    mycount = countdigitletters(str(input('Enter String: ')))
    print("Letters {}\nDigits {}".format(mycount[0], mycount[1]))


if __name__ == '__main__':
    main()
