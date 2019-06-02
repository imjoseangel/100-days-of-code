#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)

import logging
import pdb


def f(x):
    logging.error("bad vibes")
    return x / 0


def main():
    pdb.run("f(1)")


if __name__ == '__main__':
    main()
