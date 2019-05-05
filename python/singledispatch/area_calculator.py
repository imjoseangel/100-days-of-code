#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)

from functools import singledispatch
import attr


@attr.s(auto_attribs=True, frozen=True)
class Square:
    side: float


@singledispatch
def get_area(shape):
    raise NotImplementedError("cannot calculate area for unknown shape", shape)


@get_area.register(Square)
def _get_area_square(shape):
    return shape.side**2
