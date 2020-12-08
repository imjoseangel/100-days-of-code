#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


def bestSum(targetSum: int, numbers: list) -> list:

    table = [None] * (targetSum + 1)
    table[0] = []

    i = 0
    while i <= targetSum:
        try:
            if table[i] is not None:
                for num in numbers:
                    combination = [*table[i], num]
                    if not table[i + num] or len(table[i + num]) > len(combination):
                        table[i + num] = combination
        except IndexError:
            pass
        i += 1

    return table[targetSum]


def main():
    print(bestSum(7, [5, 3, 4, 7]))  # [7]
    print(bestSum(8, [2, 3, 5]))  # [5, 3]
    print(bestSum(8, [1, 4, 5]))  # [4, 4]
    print(bestSum(100, [1, 2, 5, 25]))  # [25, 25, 25, 25]


if __name__ == '__main__':
    main()
