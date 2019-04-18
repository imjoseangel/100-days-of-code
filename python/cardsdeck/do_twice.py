#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)

from typing import Callable


def do_twice(func: Callable[[str], str], argument: str) -> None:
    print(func(argument))
    print(func(argument))


def create_greeting(name: str) -> str:
    return f"Hello {name}"


def main():
    do_twice(create_greeting, "Jekyll")


if __name__ == '__main__':
    main()
