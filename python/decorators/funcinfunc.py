#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Defining functions within functions"""

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


def hi_there():
    """ Hi There Function """

    print("now you are inside the hi_there() function")

    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    print(greet())
    print(welcome())
    print("now you are back in the hi_there() function")


hi_there()

# greet()
# outputs: NameError: name 'greet' is not defined


def hi_jose(name="joseangel"):
    """ Hi Jose Function """

    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "joseangel":
        return greet

    return welcome


def hi_joseangel():
    """ Hi Jose Angel Function """

    return "hi joseangel!"


def do_somethingbeforehi(func):
    """ Do Something Before Hi Function """

    print("I am doing some boring work before executing hi()")
    print(func())


HELLOTHERE = hi_jose(name="jose")
print(HELLOTHERE)

print(HELLOTHERE())

do_somethingbeforehi(hi_joseangel)
