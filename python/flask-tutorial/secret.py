#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Create Secret Key for Flask"""

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from base64 import b64encode
from os import urandom

RANDOM_BYTES = urandom(16)
TOKEN = b64encode(RANDOM_BYTES).decode('utf-8')

print(TOKEN)
