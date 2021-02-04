#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import re


def main():
    syslogf = open('syslog', 'r')

    regex = re.compile(
        r"^((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s{1,2}\d{1,2})"
        r"\s\d{2}:\d{2}:\d{2}\s\S{1,256}\s(\S{1,256})\W\d{1,256}\W")

    lines = syslogf.readlines()
    for line in lines:
        result = regex.search(line)
        if result:
            print(result.group(1) + " " + result.group(3))


if __name__ == '__main__':
    main()
