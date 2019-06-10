#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=unused-argument

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)
# Draw text to center of screen
import curses
from curses import wrapper

screen = curses.initscr()
num_rows, num_cols = screen.getmaxyx()


# Make a function to print a line in the center of screen
def print_center(message):
    # Calculate center row
    middle_row = int(num_rows / 2)

    # Calculate center column, and then adjust starting position based
    # on the length of the message
    half_length_of_message = int(len(message) / 2)
    middle_column = int(num_cols / 2)
    x_position = middle_column - half_length_of_message

    # Draw the text
    screen.addstr(middle_row, x_position, message)
    screen.refresh()


def main(main_screen):

    print_center("Hello from the center!")

    # Clean up
    curses.nocbreak()  # Turn off cbreak mode
    curses.echo()  # Turn echo back on
    curses.curs_set(1)  # Turn cursor back on
    # If initialized like `my_screen = curses.initscr()`
    screen.keypad(0)  # Turn off keypad keys

    # Wait and cleanup
    curses.napms(3000)
    curses.endwin()


if __name__ == '__main__':
    wrapper(main)
