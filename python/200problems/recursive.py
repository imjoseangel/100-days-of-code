#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)


def sumlist(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sumlist(arr[1:])


def countlist(arr):
    if len(arr) == 0:
        return 0
    return 1 + countlist(arr[1:])


def maxinlist(arr):
    if len(arr) == 0:
        return 0
    return arr[0] if arr[0] > maxinlist(arr[1:]) else maxinlist(arr[1:])


def main():
    myarray = [300, 100, 40, 20]
    print(f'Total Sum: {sumlist(myarray)}')
    print(f'Total Count: {countlist(myarray)}')
    print(f'Max: {maxinlist(myarray)}')


if __name__ == '__main__':
    main()
