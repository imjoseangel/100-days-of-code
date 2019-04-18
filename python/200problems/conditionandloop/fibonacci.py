#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)

# Write a Python program to get the Fibonacci series between 0 to 50

import matplotlib.pyplot as plt


def fibonacciinput(maxnumber):
    fibonacci = []
    minnumber = 0
    sumnumber = 1
    while sumnumber <= maxnumber:
        fibonacci.append(sumnumber)
        minnumber, sumnumber = sumnumber, minnumber + sumnumber
    return fibonacci


def main():
    fibonacci = fibonacciinput(1000)
    print(fibonacci)
    # Use Style
    plt.style.use('fivethirtyeight')
    plt.title('Fibonacci')

    plt.plot(fibonacci)
    plt.show()


if __name__ == '__main__':
    main()
