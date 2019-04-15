#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


def timing(f):
    from functools import wraps
    from time import time
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print('Elapsed time: {}'.format(end-start))
        return result
    return wrapper


def mydec(original_function):
    def mydecorator():
        print("Hello World")
        original_function()

    return mydecorator


def time_this(original_function):
    def timer(*args, **kwargs):
        import datetime
        before = datetime.datetime.now()
        time = original_function(*args, **kwargs)
        after = datetime.datetime.now()
        print("Elapsed Time = {0}".format(after - before))
        return time

    return timer


@timing
@time_this
@mydec
def main():
    print("Hello")


if __name__ == '__main__':
    main()
