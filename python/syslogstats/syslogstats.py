#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import re


def main():
    syslogf = open('syslog', 'r')

    regex = re.compile(
        r"^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s{1,2}\d{1,2}")

    lines = syslogf.readlines()
    for line in lines:
        result = regex.search(line)
        if result:
            print(result.group(0))


if __name__ == '__main__':
    main()
