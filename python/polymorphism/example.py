#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


class Bird:
    def __init__(self):
        self.numberOfCoconuts = 10
        self.isNailed = False
        self.voltage = 10
        self.example = None

    def getBaseSpeed(self, *voltage):
        for self.example in voltage:
            yield self.example

    # ...
    def getSpeed(self):
        return self.voltage

    def getLoadFactor(self):
        return self.voltage


class European(Bird):
    def getSpeed(self):
        return self.getBaseSpeed()


class African(Bird):
    def getSpeed(self):
        return self.getBaseSpeed(
        ) - self.getLoadFactor() * self.numberOfCoconuts


class NorwegianBlue(Bird):
    def getSpeed(self):
        return 0 if self.isNailed else self.getBaseSpeed(self.voltage)


def main():

    bird = NorwegianBlue()
    # Somewhere in client code
    speed = bird.getSpeed()
    print(speed)


if __name__ == '__main__':
    main()
