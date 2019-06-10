#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)
import curses


def main():

    screen = curses.initscr()
    screen.refresh()

    # Make a pad 100 lines tall 20 chars wide
    # Make the pad large enough to fit the contents you want
    # You cannot add text larger than the pad
    # We are only going to add one line and barely use any of the space
    pad = curses.newpad(100, 100)
    pad.addstr("This text is thirty characters")

    # Start printing text from (0,2) of the pad (first line, 3rd char)
    # on the screen at position (5,5)
    # with the maximum portion of the pad displayed being 20 chars x 15 lines
    pad.refresh(0, 2, 5, 5, 15, 20)

    curses.napms(3000)
    curses.endwin()


if __name__ == '__main__':
    main()
