#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


def binary_search(listsearch, item):
    low = 0
    high = len(listsearch) - 1

    while low <= high:
        mid = round((low + high + .5) / 2)
        guess = listsearch[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


def main():
    my_list = [1, 3, 5, 7, 9]
    search = binary_search(my_list, 3)
    print(search)


if __name__ == '__main__':
    main()
