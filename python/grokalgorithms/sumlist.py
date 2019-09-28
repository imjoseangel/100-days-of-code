#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function)


def sumlist(array):
    if not array:
        return 0
    return array[0] + sumlist(array[1:])


def main():
    myarray = sumlist([1, 2, 3, 4])
    print(myarray)


if __name__ == '__main__':
    main()
