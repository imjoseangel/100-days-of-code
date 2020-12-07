#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fib(n) -> int:
    table = [0] * (n + 1)
    table[1] = 1


# this is the same as for(let i = 0; i<=n; i++) in js

    i = 0
    while i < len(table):
        try:
            table[i + 1] += table[i]
            table[i + 2] += table[i]
        except IndexError:
            pass
        i += 1

    return table[n]


print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))
