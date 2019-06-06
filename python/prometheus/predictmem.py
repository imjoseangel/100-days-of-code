#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)

import sys
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd


def main():

    sys.__stdout__ = sys.stdout

    linear_regressor = LinearRegression()

    dataset = pd.read_csv('promql.csv')
    dataset2 = pd.read_csv('promql2.csv')

    X = dataset[['replicas', 'cpu']]
    y = dataset['memory']

    X2 = dataset2[['replicas', 'cpu']]
    z2 = dataset2['replicas']

    X_train, _, y_train, _ = train_test_split(X,
                                              y,
                                              test_size=0.9,
                                              random_state=0)

    linear_regressor.fit(X_train, y_train)

    pred_y = linear_regressor.predict(X2)

    df = pd.DataFrame({'Projected Replicas': z2, 'Mem Needed': pred_y})
    print(df)


if __name__ == '__main__':
    main()
