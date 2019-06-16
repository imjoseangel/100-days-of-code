#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)


class Dog:
    num_legs = 4  # <- Class variable

    def __init__(self, name):
        self.name = name  # <- Instance variable


def main():

    jack = Dog('Jack')
    jill = Dog('Jill')
    print(jack.name, jill.name)
    print(jack.num_legs, jill.num_legs, Dog.num_legs)
    Dog.num_legs = 6
    print(jack.num_legs, jill.num_legs, Dog.num_legs)
    Dog.num_legs = 4
    jack.num_legs = 6
    print(jack.num_legs, jill.num_legs, Dog.num_legs)
    print(jack.num_legs, jack.__class__.num_legs)


if __name__ == '__main__':
    main()
