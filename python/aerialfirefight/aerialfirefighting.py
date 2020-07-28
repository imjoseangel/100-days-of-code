#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
import re
import unittest


class TestWaterbombsFunction(unittest.TestCase):
    @staticmethod
    def test_waterbombs():
        assert waterbombs('xxxxYxYx', 4) == 3
        assert waterbombs('xxYxx', 3) == 2


def bombs(situation: str, fire_width: int) -> int:
    regex = "x{1,%d}" % fire_width
    matches = re.findall(re.compile(regex), situation)

    return len(matches)


def waterbombs(pattern: str, water: int) -> int:
    count = 0
    fire = (pattern.split('Y'))
    for item in fire:
        if item:
            try:
                if (len(item) / water).is_integer():
                    count += int(len(item) / water)
                else:
                    count += int(len(item) / water) + 1
            except ValueError as value_error:
                print("ValueError: {0}".format(value_error))
            except TypeError as value_error:
                print("TypeError: {0}".format(value_error))
    return count


def main():
    pass


if __name__ == '__main__':
    main()
