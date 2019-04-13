#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

# Load Libraries
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt

# Generate feature, matrix, target vectors and true coefficients
features, target, coefficients = make_regression(n_samples=100,
                                                 n_features=3,
                                                 n_informative=3,
                                                 n_targets=1,
                                                 noise=0.0,
                                                 coef=True,
                                                 random_state=1)

# View feature matrix and target vector
print('Feature Matrix\n', features[:3])
print('Feature Vector\n', target[:3])

# Use Style
plt.style.use('fivethirtyeight')
plt.title('Make Regression')

# View plot
plt.scatter(features[:, 0], features[:, 1], c=target)
plt.show()
