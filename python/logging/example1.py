#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)

import logging
import sys


def main():
    logger = logging.getLogger("pylog")
    logger.setLevel(logging.DEBUG)
    h1 = logging.FileHandler(filename="records.log")
    h1.setLevel(logging.INFO)
    h2 = logging.StreamHandler(sys.stderr)
    h2.setLevel(logging.ERROR)
    logger.addHandler(h1)
    logger.addHandler(h2)
    logger.info("testing %d.. %d.. %d..", 1, 2, 3)


if __name__ == '__main__':
    main()
