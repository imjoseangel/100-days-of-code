#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

# Load Libraries
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Generate feature matrix and target vector
features, target = make_blobs(n_samples=100,
                              n_features=2,
                              centers=3,
                              cluster_std=0.5,
                              shuffle=True,
                              random_state=1)

# View feature matrix and target vector
print('Feature Matrix\n', features[:3])
print('Target Vector\n', target[:3])

# Use Style
plt.style.use('fivethirtyeight')
plt.title('Make Regression')

# View plot
plt.scatter(features[:, 0], features[:, 1], c=target)
plt.show()
