#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)
import curses


def main():

    screen = curses.initscr()

    screen.addstr("Hello, I will be cleared in 2 seconds.")
    screen.refresh()
    curses.napms(2000)

    # Wipe the screen buffer and set the cursor to 0,0
    screen.clear()
    screen.refresh()
    curses.napms(2000)

    curses.endwin()


if __name__ == '__main__':
    main()
