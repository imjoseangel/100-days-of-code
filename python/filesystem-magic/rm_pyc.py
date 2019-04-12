#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import sys

from fs import open_fs

with open_fs(sys.argv[1]) as fs:
    count = fs.glob("**/*.pyc").remove()
print(f"{count} .pyc files removed")
