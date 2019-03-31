#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Men Restroom Algorithm"""

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import random
import time

TIMEPEEING = 1
STALLS = 10
LIST_UNTAKEN = list(range(0, STALLS))
LIST_TAKEN = []
STR_EMPTY = "\U0001F6BD"
STR_TAKEN = "\U0001F6B6"
STALL_PRINT = list(STR_EMPTY * STALLS)


def take_stall():
    # Check if there is any empty stall
    if len(LIST_UNTAKEN) > 0:
        new_stall = random.choice(LIST_UNTAKEN)
        LIST_UNTAKEN.remove(new_stall)
        LIST_TAKEN.append(new_stall)

    STALL_PRINT.pop(LIST_TAKEN[-1])
    STALL_PRINT.insert(LIST_TAKEN[-1], STR_TAKEN)

    return LIST_UNTAKEN, LIST_TAKEN, STALL_PRINT


def leave_stall():
    # Pee done
    if len(LIST_TAKEN) > 0:
        old_stall = LIST_TAKEN[0]
        LIST_TAKEN.remove(old_stall)
        LIST_UNTAKEN.append(old_stall)
        STALL_PRINT.pop(old_stall)
        STALL_PRINT.insert(old_stall, STR_EMPTY)

    return LIST_UNTAKEN, LIST_TAKEN, STALL_PRINT


def main():

    peeing = TIMEPEEING
    while len(LIST_UNTAKEN) > 0:

        take_stall()
        for item in STALL_PRINT:
            print(item, end=' ', flush=True)
        time.sleep(1)

        if peeing == 0:
            leave_stall()
            peeing = TIMEPEEING
        else:
            peeing -= 1

        print("\n")


if __name__ == '__main__':
    main()
