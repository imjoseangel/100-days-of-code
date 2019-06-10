#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)
import curses


def main():

    print("Preparing to initialize screen...")
    screen = curses.initscr()
    print("Screen initialized.")
    screen.refresh()

    curses.napms(2000)
    curses.endwin()

    print("Window ended.")


if __name__ == '__main__':
    main()
