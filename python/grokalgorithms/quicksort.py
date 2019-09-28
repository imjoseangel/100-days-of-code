#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [item for item in array[1:] if item <= pivot]
        greater = [item for item in array[1:] if item > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


def main():
    myarray = quicksort([10, 5, 2, 3])
    print(myarray)


if __name__ == '__main__':
    main()
