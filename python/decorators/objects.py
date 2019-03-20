#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Everything in Python is an object"""

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


def hi_there(name="joseangel"):
    """ Hi There Function """

    return "hi " + name


print(hi_there())
# output: 'hi joseangel'

# We can even assign a function to a variable like
GREET = hi_there
# We are not using parentheses here because we are not calling the function
# hi_there instead we are just putting it into the greet variable. Let's try
# to run this

print(GREET())
# output: 'hi joseangel'

# Let's see what happens if we delete the old hi_there function!
del hi_there
# print(hi_there())
# outputs: NameError

print(GREET())
# outputs: 'hi yasoob'
