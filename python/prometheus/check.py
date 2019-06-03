#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)

import sys
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np
import pandas as pd


def main():

    sys.__stdout__ = sys.stdout

    linear_regressor = LinearRegression()

    dataset = pd.read_csv('promql.csv')
    print(dataset.head())

    X = dataset[['memory', 'cpu']]
    y = dataset['replicas']

    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        test_size=0.2,
                                                        random_state=0)

    linear_regressor.fit(X_train, y_train)

    coeff = pd.DataFrame(linear_regressor.coef_,
                         X.columns,
                         columns=['Coefficient'])
    print(coeff)

    pred_y = linear_regressor.predict(X_test)

    df = pd.DataFrame({'Actual': y_test, 'Predicted': pred_y})
    print(df)

    print('MAE:', metrics.mean_absolute_error(y_test, pred_y))
    print('MSE:', metrics.mean_squared_error(y_test, pred_y))
    print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, pred_y)))


if __name__ == '__main__':
    main()
