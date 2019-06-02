#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)


class NameTooShortError(ValueError):
    pass


def validate(name):
    if len(name) < 10:
        raise NameTooShortError(name)


def main():
    validate('joe')


if __name__ == '__main__':
    main()
