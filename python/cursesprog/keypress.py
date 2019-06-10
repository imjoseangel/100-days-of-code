#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)
import curses


def main():

    screen = curses.initscr()
    screen.addstr("Press any key...")
    screen.refresh()

    c = screen.getch()

    curses.endwin()

    # Convert the key to ASCII and print ordinal value
    print("You pressed {0} which is keycode {1}.".format(chr(c), c))


if __name__ == '__main__':
    main()
