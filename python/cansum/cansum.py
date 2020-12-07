#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


def canSum(targetSum: int, numbers: list, memo: dict = None) -> bool:

    if memo is None:
        memo = {}

    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False

    for num in numbers:
        remainder = targetSum - num
        if canSum(remainder, numbers, memo) is True:
            memo[targetSum] = True
            return True

    memo[targetSum] = False
    return False


def main():
    print(canSum(7, [2, 3]))  # True
    print(canSum(7, [5, 3, 4, 7]))  # True
    print(canSum(7, [2, 4]))  # False
    print(canSum(8, [2, 3, 5]))  # True
    print(canSum(300, [7, 14]))  # False


if __name__ == '__main__':
    main()
