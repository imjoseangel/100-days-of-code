#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=W0102

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

# memoization
# python object, keys will be the arg to fn, value will be the resturn value


def fib(n, memo={}):

    if n in memo:
        return memo[n]

    if n == 0:
        return 0

    if n <= 2:
        return 1

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


def main():

    print(fib(6))  # 8
    print(fib(7))  # 13
    print(fib(8))  # 21

    print(fib(50))  # 12586269025

    print('Hello!')
    print('The first 50 fibonacci numbers are:')
    print(','.join([str(fib(n)) for n in range(2000)]))


if __name__ == '__main__':
    main()
