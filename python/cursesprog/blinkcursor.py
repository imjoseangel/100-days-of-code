#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)
import curses


def main():

    screen = curses.initscr()

    curses.curs_set(0)
    screen.addstr(2, 2, "Hello, I disabled the cursor!")
    screen.refresh()
    curses.napms(3000)

    curses.curs_set(1)
    screen.addstr(3, 2, "And now the cursor is back on.")
    screen.refresh()
    curses.napms(3000)

    curses.endwin()


if __name__ == '__main__':
    main()
