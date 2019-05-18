#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)
import tensorflow as tf


def main():

    mnist = tf.keras.datasets.mnist.load_data()
    x_train, y_train = mnist[0]
    x_train = x_train / 255.0
    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(512, activation=tf.nn.relu),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10, activation=tf.nn.softmax)
    ])
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    # Train the model.
    model.fit(x_train, y_train, epochs=1)
    # Save the model to disk.
    filename = '/tmp/model'
    model.save(filename)


if __name__ == '__main__':
    main()
