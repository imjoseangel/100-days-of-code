#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Forecasting in Python with Prophet"""

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import os
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import boxcox
from scipy.special import inv_boxcox
import fbprophet

# Get File Directory
WORK_DIR = os.path.dirname((os.path.realpath(__file__)))

# Loading the json data as python dictionary
DATA = pd.read_csv(WORK_DIR + "/data/daily_orders.csv")
DATA['y'], lam = boxcox(DATA['value'])
DATA['ds'] = DATA['date']

# Creating Forecast
MYFORECAST = fbprophet.Prophet(daily_seasonality=True)
MYFORECAST.fit(DATA)
FUTURE = MYFORECAST.make_future_dataframe(periods=365)

FORECAST = MYFORECAST.predict(FUTURE)
MYFORECAST.plot(FORECAST)

# Apply inverse Box-Cox transform to specific forecast columns
FORECAST[['yhat', 'yhat_upper', 'yhat_lower']] = FORECAST[[
    'yhat', 'yhat_upper', 'yhat_lower'
]].apply(lambda x: inv_boxcox(x, lam))

# Plot Forecast
MYFORECAST.plot(FORECAST, uncertainty=False, xlabel='date')
MYFORECAST.plot_components(FORECAST)

plt.show()
