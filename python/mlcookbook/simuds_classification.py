#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

# Load Libraries
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt

# Generate features matrix and target vector
features, target = make_classification(n_samples=100,
                                       n_features=3,
                                       n_informative=3,
                                       n_redundant=0,
                                       n_classes=2,
                                       weights=[.25, .75],
                                       random_state=1)

# View feature matrix and target vector
print('Feature Matrix\n', features[:3])
print('Feature Vector\n', target[:3])

# Use Style
plt.style.use('fivethirtyeight')
plt.title('Make Classification')

# View plot
plt.scatter(features[:, 0], features[:, 1], c=target)
plt.show()
