#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import pandas as pd


class IrisLR():
    def __init__(self):

        iris = load_iris()

        self.X = iris.data
        self.y = iris.target
        self.x_train = None
        self.x_test = None
        self.y_train = None
        self.y_test = None
        self.log_reg = None
        self.W = None
        self.b = None

    def prepare_data(self):

        df = pd.DataFrame(self.X,
                          columns=[
                              'sepal_lenght(cm)', 'sepal_width(cm)',
                              'petal_lenght(cm)', 'petal_width(cm)'
                          ])

        df['species_id'] = self.y

        species_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
        df['species_name'] = df['species_id'].map(species_map)

        perm = np.random.permutation(len(self.X))
        df = df.loc[perm]
        print(df.head().to_string())

        setosa_mask = df['species_name'] == 'setosa'
        print(df[setosa_mask].describe().to_string())

        virginica_mask = df['species_name'] == 'virginica'
        print(df[virginica_mask].describe().to_string())

        versicolor_mask = df['species_name'] == 'versicolor'
        print(df[versicolor_mask].describe().to_string())

        # Setosa is much smaller in sepal length and petal_width when compared
        # to the other 2 species. We can also see that it has a larger
        # sepal_width on average

        plt.scatter(self.X[:, 0], self.X[:, 3], c=self.y, cmap='Dark2')
        plt.xlabel('Sepal Lenght cm')
        plt.ylabel('Petal Width cm')

        # Setosa is easily distinguished in Aqua Green on the bottom left
        plt.show()

        self.X = np.c_[self.X[:, 0], self.X[:, 3]]
        self.y = []

        for item in range(len(self.X)):
            if item < 50:
                self.y.append(1)
            else:
                self.y.append(0)

        self.y = np.array(self.y)

        plt.scatter(self.X[:, 0], self.X[:, 1], c=self.y)
        plt.show()

        self.x_train, self.x_test = self.X[perm][20:], self.X[perm][:20]
        self.y_train, self.y_test = self.y[perm][20:], self.y[perm][:20]

        print(self.x_train.shape, self.y_train.shape, self.x_test.shape,
              self.y_test.shape)

    def analyze_data(self):

        self.log_reg = LogisticRegression()
        print(self.log_reg.fit(self.X, self.y))
        self.W, self.b = self.log_reg.coef_, self.log_reg.intercept_
        print(self.W, self.b)

        probas = self.log_reg.predict_proba(self.x_train)
        print(probas[0:10])

        plt.scatter(self.X[:, 0], self.X[:, 1], c=self.y)
        ax = plt.gca()
        ax.autoscale = False
        xvals = np.array(ax.get_xlim())
        yvals = -(xvals * self.W[0][0] + self.b) / self.W[0][1]
        plt.plot(xvals, yvals)
        plt.show()

    def predict_data(self):
        predictions = self.log_reg.predict(self.x_test)
        print(predictions)
        print(self.y_test)

        plt.scatter(self.x_test[:, 0], self.x_test[:, 1], c=self.y_test)
        ax = plt.gca()
        xvals = np.array(ax.get_xlim())
        yvals = -(xvals * self.W[0][0] + self.b) / self.W[0][1]
        plt.plot(xvals, yvals)
        plt.show()


def main():

    run_logistic = IrisLR()
    run_logistic.prepare_data()
    run_logistic.analyze_data()
    run_logistic.predict_data()


if __name__ == '__main__':
    main()
