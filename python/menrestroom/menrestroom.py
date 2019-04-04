#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Men Restroom Algorithm"""

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import random
import time
import threading

STALLFREQ = 1
TIMEPEEING = 30
STALLS = 10
LIST_UNTAKEN = list(range(0, STALLS))
LIST_TAKEN = []
ODD_LIST = []
EVEN_LIST = []
STR_EMPTY = "\U0001F6BD"
STR_TAKEN = "\U0001F6B6"
STALL_PRINT = list(STR_EMPTY * STALLS)


def oddeven_list(takenlist):
    for number in takenlist:
        # checking condition
        if number % 2 != 0:
            ODD_LIST.append(number)
        else:
            EVEN_LIST.append(number)

    return ODD_LIST, EVEN_LIST


def take_stall():
    # Check if there is any empty stall
    if len(LIST_UNTAKEN) > 0:
        if not LIST_TAKEN:
            new_stall = round(sum(LIST_UNTAKEN) / len(LIST_UNTAKEN) + .5)
        else:
            new_stall = random.choice(LIST_UNTAKEN)
            # if (new_stall + 1) or (new_stall - 1) in LIST_TAKEN:
            #     print(new_stall)
            #     new_stall = random.choice(LIST_UNTAKEN)
            #     print(new_stall)
        LIST_UNTAKEN.remove(new_stall)
        LIST_TAKEN.append(new_stall)

    STALL_PRINT.pop(LIST_TAKEN[-1])
    STALL_PRINT.insert(LIST_TAKEN[-1], STR_TAKEN)

    threading.Timer(STALLFREQ, take_stall).start()

    return LIST_UNTAKEN, LIST_TAKEN, STALL_PRINT


def leave_stall():
    # Pee done
    if len(LIST_TAKEN) > 0:
        old_stall = LIST_TAKEN[0]
        LIST_TAKEN.remove(old_stall)
        LIST_UNTAKEN.append(old_stall)
        STALL_PRINT.pop(old_stall)
        STALL_PRINT.insert(old_stall, STR_EMPTY)

    threading.Timer(TIMEPEEING, leave_stall).start()

    return LIST_UNTAKEN, LIST_TAKEN, STALL_PRINT


def main():

    # peeing = threading.Timer(5.0, leave_stall)
    take_stall()
    leave_stall()

    while len(LIST_UNTAKEN) > 0:
        for item in STALL_PRINT:
            print(item, end=' ', flush=True)

        time.sleep(STALLFREQ)
        print('\n')


if __name__ == '__main__':
    main()
