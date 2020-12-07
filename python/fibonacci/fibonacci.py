#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


print('Hello!')
print('The first 50 fibonacci numbers are:')
print(','.join([str(fib(n)) for n in range(50)]))
