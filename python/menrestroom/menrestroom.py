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
        self.untaken = list(range(0, stalls))
        self.taken = []
        self.new_stall = round(sum(self.untaken) / len(self.untaken) + .5)
        self.emo_empty = "\U0001F6BD"
        self.emo_taken = "\U0001F6B6"
        self.stall_print = list(self.emo_empty * stalls)

        self.take_stall()
        self.leave_stall()

    # def oddsevens(self, stalls):
    #     for number in stalls:
    #         # checking condition
    #         if number % 2 != 0:
    #             self.odds.append(number)
    #         else:
    #             self.evens.append(number)

    #     if self.new_stall % 2 != 0:
    #         self.odds.remove(self.new_stall)
    #         self.stallisodd = True
    #     else:
    #         self.evens.remove(self.new_stall)
    #         self.stallisodd = False

    def take_stall(self):
        # Check if there is any empty stall
        if len(self.untaken) > 0:
            if not self.taken:
                new_stall = self.new_stall
            else:
                new_stall = random.choice(self.untaken)
            self.untaken.remove(new_stall)
            self.taken.append(new_stall)

        self.stall_print.pop(self.taken[-1])
        self.stall_print.insert(self.taken[-1], self.emo_taken)

        threading.Timer(self.stallfreq, self.take_stall).start()

        return self.untaken, self.taken, self.stall_print

    def leave_stall(self):
        # Pee done
        if len(self.taken) > 0:
            old_stall = self.taken[0]
            self.taken.remove(old_stall)
            self.untaken.append(old_stall)
            self.stall_print.pop(old_stall)
            self.stall_print.insert(old_stall, self.emo_empty)

        threading.Timer(self.timepeeing, self.leave_stall).start()

        return self.untaken, self.taken, self.stall_print


def main():

    newpee = Menpeeing(stalls=10, stallfreq=1)

    while len(newpee.untaken) > 0:
        for item in newpee.stall_print:
            print(item, end=' ', flush=True)

        time.sleep(newpee.stallfreq)
        print('\n')


if __name__ == '__main__':
    main()
