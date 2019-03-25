#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Socker Programming - Multi Connection Server"""

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(444)
fig, _ = plt.subplots()
print(type(fig))

one_tick = fig.axes[0].yaxis.get_major_ticks()[0]
print(type(one_tick))
