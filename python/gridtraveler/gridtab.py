#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


def gridTraveler(m, n):

    table = [[0 for i in range(n + 1)] for j in range(m + 1)]

    table[1][1] = 1

    i = 0
    while i <= m:
        j = 0
        while j <= n:
            current = table[i][j]
            if (j + 1) <= n:
                table[i][j + 1] += current
            if (i + 1) <= m:
                table[i + 1][j] += current
            j += 1
        i += 1

    return table[m][n]


def main():
    print(gridTraveler(1, 1))  # 1
    print(gridTraveler(2, 3))  # 3
    print(gridTraveler(3, 2))  # 3
    print(gridTraveler(3, 3))  # 6
    print(gridTraveler(18, 18))  # 2333606220


if __name__ == '__main__':
    main()
