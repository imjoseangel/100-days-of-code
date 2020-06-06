#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C0116, C0114, W0613

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import toga


def button_handler(widget):
    print("hello")


def build(app):
    box = toga.Box()

    button = toga.Button('Hello world', on_press=button_handler)
    button.style.padding = 50
    button.style.flex = 1
    box.add(button)

    return box


def main():
    return toga.App('First App', 'org.beeware.helloworld', startup=build)


if __name__ == '__main__':
    main().main_loop()
