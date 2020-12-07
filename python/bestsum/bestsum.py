#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


def bestSum(targetSum: int, numbers: list, memo: dict = None) -> list:

    if memo is None:
        memo = {}

    if targetSum in memo:
        return memo[targetSum]

    if targetSum == 0:
        return []

    if targetSum < 0:
        return None

    shortestCombination = None

    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSum(remainder, numbers, memo)
        if remainderCombination is not None:
            combination = [*remainderCombination, num]
            # if the combination is shorter then the current "shortest", update it
            if shortestCombination is None or len(combination) < len(shortestCombination):
                shortestCombination = combination

    memo[targetSum] = shortestCombination
    return shortestCombination


# m = target num
# n = numbers.length
#
# Brute Force
# time: O(n^m * m)
# space: O(m)
#
# Memoized
# time: O(n*m^2)
# space: O(m^2)

def main():
    print(bestSum(7, [5, 3, 4, 7]))  # [7]
    print(bestSum(8, [2, 3, 5]))  # [5, 3]
    print(bestSum(8, [1, 4, 5]))  # [4, 4]
    print(bestSum(100, [1, 2, 5, 25]))  # [25, 25, 25, 25]


if __name__ == '__main__':
    main()
