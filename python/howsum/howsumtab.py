#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


def howSum(targetSum: int, numbers: list) -> list:

    table = [None] * (targetSum + 1)
    table[0] = []

    i = 0
    while i <= targetSum:
        try:
            if table[i] is not None:
                for num in numbers:
                    table[i + num] = [*table[i], num]
        except IndexError:
            pass
        i += 1

    return table[targetSum]


def main():
    print(howSum(7, [2, 3]))  # [3, 2, 2]
    print(howSum(7, [5, 3, 4, 7]))  # [7]
    print(howSum(7, [2, 4]))  # None
    print(howSum(8, [2, 3, 5]))  # [2, 2, 2, 2]
    print(howSum(300, [7, 14]))  # None


if __name__ == '__main__':
    main()
