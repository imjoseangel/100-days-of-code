#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)

# Count the number of even and odd numbers from a series of numbers
# Input
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
# Output
# Number of even numbers : 4
# Number of odd numbers : 5


def countevenodd(mytyple):
    even = 0
    odd = 0
    for item in mytyple:
        if item % 2:
            even += 1
        else:
            odd += 1
    return even, odd


def main():
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    mycount = countevenodd(numbers)
    print("Number of even numbers : {}\nNumber of odd numbers : {}".format(
        mycount[0], mycount[1]))


if __name__ == '__main__':
    main()
