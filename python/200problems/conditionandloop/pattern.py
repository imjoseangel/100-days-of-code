#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Write a Python program to construct the following pattern,
# using a nested for loop.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

asteriskno = 5


def main():

    for asterisk in range(1, asteriskno):
        print(asterisk * '* ')
    for asterisk in reversed(range(1, asteriskno + 1)):
        print(asterisk * '* ')


if __name__ == '__main__':
    main()
