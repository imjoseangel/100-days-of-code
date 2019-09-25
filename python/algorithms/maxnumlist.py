#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function)


def maxlist(array):
    if not array:
        return 0
    elif len(array) == 1:
        return array[0]
    elif len(array) == 2:
        return array[0] if array[0] > array[1] else array[1]
    sub_max = maxlist(array[1:])
    return array[0] if array[0] > sub_max else sub_max


def main():
    myarray = maxlist([1, 40, 5, 2])
    print(myarray)


if __name__ == '__main__':
    main()
