#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)
import curses
import subprocess
import os


def main():

    # Create a screen and print hello
    screen = curses.initscr()
    screen.addstr("Hello! Dropping you in to a command prompt...\n")
    print("Program initialized...")
    screen.refresh()
    curses.napms(2000)

    # Hide the screen, show original terminal, restore cursor position
    curses.endwin()

    # Update screen in background
    screen.clear()
    screen.addstr("I'll be waiting when you get back.\n")

    # Drop the user in a command prompt
    print("About to open command prompt...")
    curses.napms(2000)

    if os.name == 'nt':
        shell = 'cmd.exe'
    else:
        shell = 'sh'
    subprocess.call(shell)

    # When the subprocess ends, return to our screen.
    # also restoring cursor position
    screen.refresh()
    curses.napms(2000)

    # Finally go back to the terminal for real
    curses.endwin()


if __name__ == '__main__':
    main()
