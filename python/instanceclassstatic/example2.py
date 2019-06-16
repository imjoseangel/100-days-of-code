#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)
import math


class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.radius!r}, ' f'{self.ingredients!r})'

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r**2 * math.pi

    @classmethod
    def margherita(cls):
        return cls(4, ['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(4, ['mozzarella', 'tomatoes', 'ham'])


def main():
    print(Pizza(4, ['cheese', 'tomatoes']))
    print(Pizza.margherita())
    print(Pizza.prosciutto())
    p = Pizza(4, ['mozzarella', 'tomatoes'])
    print(p)
    print(p.area())
    print(p.circle_area(4))


if __name__ == '__main__':
    main()
