#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from behave.__main__ import main as behave_main


def main():
    # behave_main(["ssl.feature", "-t @run", "-k"])
    behave_main(["ssl.feature"])


if __name__ == '__main__':
    main()
