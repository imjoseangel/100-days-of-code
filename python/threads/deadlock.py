#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import threading

threadinglock = threading.Lock()
print("before first acquire")
threadinglock.acquire()
print("before second acquire")
threadinglock.acquire()
print("acquired lock twice")
