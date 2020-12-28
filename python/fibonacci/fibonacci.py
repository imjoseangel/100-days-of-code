#!/usr/bin/env python
# -*- coding: utf-8 -*-

def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func


@memoize
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


print('Hello!')
print('The first 50 fibonacci numbers are:')
print(','.join([str(fib(n)) for n in range(50)]))
