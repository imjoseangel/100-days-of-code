#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)
from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    @abstractmethod
    def basefoo(self):
        pass

    @abstractmethod
    def basebar(self):
        pass


class Concrete(Base):
    def basefoo(self):
        pass

    def basebar(self):
        pass


def main():

    c = Concrete()
    print(c.basefoo())


if __name__ == '__main__':
    main()
