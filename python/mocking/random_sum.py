#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import random


def sum_numbers_add_random_int(nums=None):
    total = sum(nums)

    total += random.randint(1, 100)
    return total


def main():
    print(sum_numbers_add_random_int([1, 2, 3]))


if __name__ == '__main__':
    main()
