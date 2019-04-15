#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

# def timing(original_function):
#     from functools import wraps
#     from time import time

#     @wraps(original_function)
#     def wrapper(*args, **kwargs):
#         start = time()
#         result = original_function(*args, **kwargs)
#         end = time()
#         print('Elapsed time: {}'.format(end - start))
#         return result

#     return wrapper


def time_this(original_function):
    def timer(*args, **kwargs):
        import datetime
        before = datetime.datetime.now()
        time = original_function(*args, **kwargs)
        after = datetime.datetime.now()
        print("Elapsed Time = {0}".format(after - before))
        return time

    return timer


def binary_search(listsearch, item):
    low = 0
    high = len(listsearch) - 1

    while low <= high:
        mid = round((low + high + .5) / 2)
        guess = listsearch[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


@time_this
def main():
    my_list = list(range(1, 10000000))
    print(binary_search(my_list, 9999))


if __name__ == '__main__':
    main()
