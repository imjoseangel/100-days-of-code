#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)

import random

PLUGINS = dict()


def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func


@register
def say_hello(name):
    return f"Hello {name}"


@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)


def main():
    print(PLUGINS)
    print(randomly_greet("Alice"))
    print(globals())


if __name__ == '__main__':
    main()
