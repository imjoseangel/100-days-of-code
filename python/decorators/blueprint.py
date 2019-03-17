#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""BluePrint"""

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from functools import wraps


def decorator_name(function):
    """ This is my new decorator function """

    @wraps(function)
    def decorated(*args, **kargs):
        if not CAN_RUN:
            return "Function will not run"
        return function(*args, **kargs)

    return decorated


@decorator_name
def func():
    """ This is my new decorated function """
    return "Function is running"


CAN_RUN = True
print(func())

CAN_RUN = False
print(func())
