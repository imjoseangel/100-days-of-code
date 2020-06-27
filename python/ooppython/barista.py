#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


class barista:

    def __init__(self, preference):
        self.str1 = "ion"
        self.str2 = self.reverse("rcne")
        self.str3 = "ypt"
        self.preference = preference

    @staticmethod
    def reverse(string):
        return ''.join(reversed(string))

    def request(self):
        return self.preference + " Secret word: {0}{1}{2}".format(self.str2, self.str3, self.str1)


def main():
    your_drink = "Coffee"
    result = barista(your_drink).request()
    print(result)


if __name__ == '__main__':
    main()
