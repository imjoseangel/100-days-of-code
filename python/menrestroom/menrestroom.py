#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Men Restroom Algorithm"""

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import random
import time
import threading


class Menpeeing:
    def __init__(self, stalls=10, stallfreq=1):
        self.stallfreq = stallfreq
        self.timepeeing = random.randint(10, 30)
        self.list_untaken = list(range(0, stalls))
        self.list_taken = []
        self.odd_list = []
        self.even_list = []
        self.str_empty = "\U0001F6BD"
        self.str_taken = "\U0001F6B6"
        self.stall_print = list(self.str_empty * stalls)

        self.take_stall()
        self.leave_stall()

    def oddeven_list(self, takenlist):
        for number in takenlist:
            # checking condition
            if number % 2 != 0:
                self.odd_list.append(number)
            else:
                self.even_list.append(number)

        return self.odd_list, self.even_list

    def take_stall(self):
        # Check if there is any empty stall
        if len(self.list_untaken) > 0:
            if not self.list_taken:
                new_stall = round(
                    sum(self.list_untaken) / len(self.list_untaken) + .5)
            else:
                new_stall = random.choice(self.list_untaken)
            self.list_untaken.remove(new_stall)
            self.list_taken.append(new_stall)

        self.stall_print.pop(self.list_taken[-1])
        self.stall_print.insert(self.list_taken[-1], self.str_taken)

        threading.Timer(self.stallfreq, self.take_stall).start()

        return self.list_untaken, self.list_taken, self.stall_print

    def leave_stall(self):
        # Pee done
        if len(self.list_taken) > 0:
            old_stall = self.list_taken[0]
            self.list_taken.remove(old_stall)
            self.list_untaken.append(old_stall)
            self.stall_print.pop(old_stall)
            self.stall_print.insert(old_stall, self.str_empty)

        threading.Timer(self.timepeeing, self.leave_stall).start()

        return self.list_untaken, self.list_taken, self.stall_print


def main():

    newpee = Menpeeing(stalls=10, stallfreq=1)

    while len(newpee.list_untaken) > 0:
        for item in newpee.stall_print:
            print(item, end=' ', flush=True)

        time.sleep(newpee.stallfreq)
        print('\n')


if __name__ == '__main__':
    main()
