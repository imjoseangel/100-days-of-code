#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Write a Python program to construct the following pattern,
# using a nested loop number.
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


def main():

    number = 1
    while number < 10:
        print(str(number) * number)
        number += 1

    number = 1
    for number in range(10):
        print(str(number) * number)


if __name__ == '__main__':
    main()
