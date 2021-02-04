#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


def main():
    syslogf = open('syslog', 'r')

    lines = syslogf.readlines()
    print(lines)


if __name__ == '__main__':
    main()
