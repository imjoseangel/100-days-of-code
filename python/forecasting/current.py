#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Forecasting in Python with Prophet"""

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import os
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import boxcox

# Get File Directory
WORK_DIR = os.path.dirname((os.path.realpath(__file__)))

# Loading the json data as python dictionary
DATA = pd.read_csv(WORK_DIR + "/data/daily_orders.csv")
DATA.date = pd.to_datetime(DATA['date'], format='%Y-%m-%d %H:%M:%S')
DATA['boxcox'], lam = boxcox(DATA['value'])

# inplace is mandatory here. Have to assign back to dataframe
# (because it is a new copy)
DATA.set_index('date', inplace=True)

# Print DATA
DATA.plot(subplots=True, layout=(2, 1), figsize=(9, 9))
plt.show()
