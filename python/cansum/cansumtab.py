#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


def canSum(targetSum: int, numbers: list) -> bool:

    table = [False] * (targetSum + 1)
    table[0] = True

    i = 0
    while i <= targetSum:
        try:
            if table[i] is True:
                for num in numbers:
                    table[i + num] = True
        except IndexError:
            pass
        i += 1

    return table[targetSum]


def main():
    print(canSum(7, [2, 3]))  # True
    print(canSum(7, [5, 3, 4, 7]))  # True
    print(canSum(7, [2, 4]))  # False
    print(canSum(8, [2, 3, 5]))  # True
    print(canSum(300, [7, 14]))  # False


if __name__ == '__main__':
    main()
