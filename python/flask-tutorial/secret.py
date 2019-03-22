#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Defining functions within functions"""

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from base64 import b64encode
from os import urandom

random_bytes = urandom(16)
token = b64encode(random_bytes).decode('utf-8')

print(token)
