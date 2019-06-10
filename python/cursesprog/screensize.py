#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)
import curses


def main():

    screen = curses.initscr()
    num_rows, num_cols = screen.getmaxyx()
    curses.endwin()

    print("Rows:    {0}".format(num_rows))
    print("Columns: {0}".format(num_cols))


if __name__ == '__main__':
    main()
