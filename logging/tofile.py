#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=logging-format-interpolation

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from logzero import logger, logfile


def main():

    logfile('test.log', maxBytes=1e6, backupCount=3)

    a = 1
    b = 0

    try:
        a / b
    except ZeroDivisionError as e:
        # logger.exception(e)
        logger.error("{0}: {1}".format(e.__class__.__name__, e))


if __name__ == '__main__':
    main()
