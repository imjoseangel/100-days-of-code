#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)

import math
import attr
from area_calculator import get_area, Square


@attr.s(auto_attribs=True, frozen=True)
class Ellipse:
    horizontal_axis: float
    vertical_axis: float


@get_area.register(Ellipse)
def _get_area_ellipse(shape):
    return math.pi * shape.horizontal_axis * shape.vertical_axis


def main():
    shape = Square(20)
    print(get_area(shape))


if __name__ == '__main__':
    main()
