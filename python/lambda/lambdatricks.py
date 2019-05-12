#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=unnecessary-lambda

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)

from operator import itemgetter


class Car:
    # Harmful:
    rev = lambda self: print('Wroom!')  # noqa: E731
    crash = lambda self: print('Boom!')  # noqa: E731


def main():

    # One line lambda
    print((lambda x, y: x + y)(5, 3))

    tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
    print(sorted(tuples, key=lambda x: x[1]))
    print(sorted(tuples, key=itemgetter(1)))

    print(sorted(range(-5, 6), key=lambda x: x * x))
    print(sorted(range(-5, 6), key=lambda x: abs(x)))

    my_car = Car()
    my_car.crash()

    # Harmful:
    print(list(filter(lambda x: x % 2 == 0, range(16))))

    # Better:
    print([x for x in range(16) if x % 2 == 0])


if __name__ == '__main__':
    main()
