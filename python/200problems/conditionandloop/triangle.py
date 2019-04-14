#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Write a Python program to check a triangle is valid or not

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


def triangle(a, b, c):
    if (a + b) > c and (b + c) > a and (a + c) > b:
        return True
    return False


def main():
    side1 = int(input('enter side 1: '))
    side2 = int(input('enter side 2: '))
    side3 = int(input('enter side 1: '))

    if side1 > 0 and side2 > 0 and side3 > 0:
        mytriangle = triangle(side1, side2, side3)
        if mytriangle:
            print("This is a valid Triangle")
        else:
            print("The sum of two sides must be larger than the third")
    else:
        print("Please provide 3 positive values")


if __name__ == '__main__':
    main()
