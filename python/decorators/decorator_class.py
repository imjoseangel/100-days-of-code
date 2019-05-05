#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)
from decorators import debug, timer


class TimeWaster:
    @debug
    def __init__(self, max_num):
        self.max_num = max_num

    @timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Get value of radius"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set radius, raise error if negative"""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    @property
    def area(self):
        """Calculate area inside circle"""
        return self.pi() * self.radius**2

    def cylinder_volume(self, height):
        """Calculate volume of cylinder with circle as base"""
        return self.area * height

    @classmethod
    def unit_circle(cls):
        """Factory method creating a circle with radius 1"""
        return cls(1)

    @staticmethod
    def pi():
        """Value of π, could use math.pi instead though"""
        return 3.1415926535


def main():
    c = Circle(5)
    print(c.radius)
    print(c.area)
    c.radius = 2
    print(c.area)
    # c.area = 100 # AttributeError: can't set attribute
    print(c.cylinder_volume(height=4))
    # c.radius = -1 # ValueError: Radius must be positive

    c = Circle.unit_circle()
    print(c.radius)
    print(c.pi())
    print(Circle.pi())

    tw = TimeWaster(1000)
    tw.waste_time(999)


if __name__ == '__main__':
    main()
