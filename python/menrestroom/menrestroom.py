#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Men Restroom Algorithm"""

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import random
import time
import threading


class Menpeeing:
    def __init__(self,
                 stalls=10,
                 stallfreq=2,
                 mintimepeeing=1,
                 maxtimepeeing=10):
        self.stallfreq = stallfreq
        self.mintimepeeing = mintimepeeing
        self.maxtimepeeing = maxtimepeeing
        self.timepeeing = random.randint(self.mintimepeeing,
                                         self.maxtimepeeing)
        self.untaken = list(range(0, stalls))
        self.taken = []
        self.new_stall = round(sum(self.untaken) / len(self.untaken) + .5)
        self.left = self.untaken[1:self.new_stall:2]
        self.right = self.untaken[self.new_stall + 2::2]
        self.emo_empty = "\U0001F6BD"
        self.emo_taken = "\U0001F6B6"
        self.emo_door = "\U0001F6AA"
        self.stall_print = list(self.emo_empty * stalls + self.emo_door)

        self.take_stall()
        self.leave_stall()

    def take_stall(self):
        # Check if there is any empty stall
        if self.untaken:
            if not self.taken:
                new_stall = self.new_stall
            else:
                if self.left:
                    new_stall = random.choice(self.left)
                    self.left.remove(new_stall)
                elif self.right:
                    new_stall = random.choice(self.right)
                    self.right.remove(new_stall)
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
        if self.taken:
            old_stall = self.taken[0]
            self.taken.remove(old_stall)
            self.untaken.append(old_stall)
            self.stall_print.pop(old_stall)
            self.stall_print.insert(old_stall, self.emo_empty)
            self.timepeeing = random.randint(self.mintimepeeing,
                                             self.maxtimepeeing)

        threading.Timer(self.timepeeing, self.leave_stall).start()

        return self.untaken, self.taken, self.stall_print


def main():

    newpee = Menpeeing(stalls=10, stallfreq=1)

    while newpee.untaken:
        for item in newpee.stall_print:
            print(item, end=' ', flush=True)

        time.sleep(newpee.stallfreq)
        print('\n')


if __name__ == '__main__':
    main()
