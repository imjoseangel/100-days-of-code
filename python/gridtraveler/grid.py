#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=W0102

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


def gridTraveler(m, n, memo={}):

    # are the args in the memo
    key = str(m) + ',' + str(n)

    if key in memo:
        return memo[key]

    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0

    memo[key] = gridTraveler(m - 1, n, memo) + gridTraveler(m, n - 1, memo)
    return memo[key]


def main():
    print(gridTraveler(1, 1))  # 1
    print(gridTraveler(2, 3))  # 3
    print(gridTraveler(3, 2))  # 3
    print(gridTraveler(3, 3))  # 6
    print(gridTraveler(18, 18))  # 2333606220


if __name__ == '__main__':
    main()
