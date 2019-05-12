#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=blacklisted-name

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)

import functools


def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


class AlwaysBlueCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = 'blue'


def trace(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        print(f, args, kwargs)
        result = f(*args, **kwargs)
        print(result)

    return decorated_function


@trace
def greet(greeting, name):
    return '{}, {}!'.format(greeting, name)


def main():
    foo('hello', 1, 2, 3, key1='value', key2=999)
    mycar = AlwaysBlueCar('green', 48392).color
    print(mycar)
    greet('Hello', 'Bob')


if __name__ == '__main__':
    main()
