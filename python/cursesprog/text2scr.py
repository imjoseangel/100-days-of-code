#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)
import curses


def main():

    screen = curses.initscr()

    # Update the buffer, adding text at different locations
    screen.addstr(0, 0, "This string gets printed at position (0, 0)")
    screen.addstr(3, 1,
                  "Try Russian text: Привет")  # Python 3 required for unicode
    screen.addstr(4, 4, "X")
    screen.addch(5, 5, "Y")

    # Changes go in to the screen buffer and only get
    # displayed after calling `refresh()` to update
    screen.refresh()

    curses.napms(3000)
    curses.endwin()


if __name__ == '__main__':
    main()
