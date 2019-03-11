#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Krypton Level 0 → Level 1"""

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import base64

DECODE_PASSWORD = base64.b64decode('S1JZUFRPTklTR1JFQVQ=').decode('UTF-8')

print(DECODE_PASSWORD)
