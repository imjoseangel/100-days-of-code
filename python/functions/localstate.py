#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)


def get_speak_func(text, volume):
    def whisper():
        return text.lower() + '...'

    def yell():
        return text.upper() + '!'

    if volume > 0.5:
        return yell
    return whisper


def make_adder(n):
    def add(x):
        return x + n

    return add


class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n + x


def main():
    print(get_speak_func('Hello, World', 0.7)())
    print(make_adder(3)(4))

    plus_5 = make_adder(5)
    print(plus_5(4))

    print(Adder(5)(4))
    plus_3 = Adder(3)
    print(plus_3(4))

    print(callable(plus_3))
    print(callable(get_speak_func))
    print(callable('Hello'))


if __name__ == '__main__':
    main()
