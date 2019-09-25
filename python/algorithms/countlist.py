#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function)


def countlist(array):
    if not array:
        return 0
    return 1 + countlist(array[1:])


def main():
    myarray = countlist([1, 2, 3, 4])
    print(myarray)


if __name__ == '__main__':
    main()
