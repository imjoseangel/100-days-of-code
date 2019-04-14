#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

# Write a Python program which takes two digits
# m (row) and n (column) as input and generates a two-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note :
# i = 0,1.., m-1
# j = 0,1, n-1.
# Input
# Input number of rows: 3
# Input number of columns: 4
# Output
# [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]


def array(rows, columns):
    multi_list = [[0 for col in range(columns)] for row in range(rows)]
    for row in range(rows):
        for col in range(columns):
            multi_list[row][col] = row * col
    return multi_list


def main():

    row_num = int(input("Input number of rows: "))
    col_num = int(input("Input number of columns: "))
    output = array(row_num, col_num)
    print(output)


if __name__ == '__main__':
    main()
