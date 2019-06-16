#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)


class CountedObject:
    num_instances = 0

    def __init__(self):
        self.__class__.num_instances += 1


def main():
    print(CountedObject.num_instances)
    print(CountedObject().num_instances)
    print(CountedObject().num_instances)
    print(CountedObject().num_instances)
    print(CountedObject.num_instances)


if __name__ == '__main__':
    main()
