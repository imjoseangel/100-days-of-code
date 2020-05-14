#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from collections import OrderedDict
from bcoding import bdecode
from bcoding import bencode


def main():
    # An integer value starts with an 'i' followed by a series of
    # digits until terminated with a 'e'.
    print(bdecode(b'i123e'))
    # 123

    # A string value, starts by defining the number of characters
    # contained in the string, followed by the actual string.
    # Notice that the string returned is a binary string, not unicode.
    print(bdecode(b'12:Middle Earth'))
    # 'Middle Earth'

    # A list starts with a 'l' followed by any number of objects, until
    # terminated with an 'e'.
    # As in Python, a list may contain any type of object.
    print(bdecode(b'l4:spam4:eggsi123ee'))
    # ['spam', 'eggs', 123]

    # A dict starts with a 'd' and is terminated with a 'e'. objects
    # in between those characters must be pairs of string + object.
    # The order is significant in a dict, thus OrderedDict (from
    # Python 3.1) is used.
    print(bdecode(b'd3:cow3:moo4:spam4:eggse'))
    # {'cow': 'moo', 'spam': 'eggs'}

    print(bencode(123))
    # b'i123e'

    print(bencode('Middle Earth'))
    # b'12:Middle Earth'

    print(bencode(['spam', 'eggs', 123]))
    # b'l4:spam4:eggsi123ee'

    d = OrderedDict()
    d['cow'] = 'moo'
    d['spam'] = 'eggs'
    print(bencode(d))
    # b'd3:cow3:moo4:spam4:eggse'


if __name__ == '__main__':
    main()
