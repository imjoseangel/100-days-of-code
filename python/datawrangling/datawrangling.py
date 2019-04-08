#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import os
import pandas as pd
import numpy as np

# Get File Directory
WORK_DIR = os.path.dirname((os.path.realpath(__file__)))

# Loading the json data as python dictionary
df = pd.read_csv(WORK_DIR + "/data/titanic.csv")
head = df.head()
dropna = df.dropna()

over30 = df[df['Age'] > 30]
female = df[df['Sex'] == 'female']
over30female = df[(df['Age'] > 30) & (df['Sex'] == 'female')]

print(over30female)

bysex = df.groupby('Sex').Survived.value_counts()

print(bysex)

# Create an array of 200 elements at the interval of 1 sec.
data = pd.date_range('1/1/2016', periods=150, freq='s')

# Let's create timeseries data by assigning random values to
# integer to each values in data

time_series = pd.Series(np.random.randint(0, 500, len(data)), index=data)
print(time_series.head())
print("\n")

# Resample: bin 1 sec raws to minutes and summing the corresponding values
time_series = time_series.resample('1Min').sum()
print(time_series.head())
print("\n")

# Time zone conversion: Let's assume original timeseries was
# in UTC and we want to convert to US/Eastern

time_series_utc = time_series.tz_localize('UTC')
time_series_utc.tz_convert('US/Eastern')

result = df[(df['Age'] > 30) & (df['Sex'] == 'female')]
result.to_excel('result.xlsx')
