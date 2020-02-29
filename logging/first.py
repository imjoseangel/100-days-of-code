#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from logzero import logger


def main():

    logger.debug("hello")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")


if __name__ == '__main__':
    main()
