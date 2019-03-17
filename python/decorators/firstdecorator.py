#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""My First Decorator"""

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from functools import wraps


def a_new_decorator(a_func):
    """ This is my new decorator function """

    @wraps(a_func)
    def wrap_thefunction():
        """ This is my function wrapper """

        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doing some boring work after executing a_func()")

    return wrap_thefunction


def a_function_requiring_decoration():
    """ This is my function which requires decorator """

    print(
        "I am the function which needs some decoration to remove my foul smell"
    )


FUNCTION = a_new_decorator(a_function_requiring_decoration)

FUNCTION()


@a_new_decorator
def another_function_requiring_decoration():
    """Hey you! Decorate me!"""

    print(
        "I am the function which needs some decoration to remove my foul smell"
    )


another_function_requiring_decoration()

print(another_function_requiring_decoration.__name__)
