#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)
from multiprocessing import Pool
import sys
import psutil
import tensorflow as tf

num_cpus = psutil.cpu_count(logical=False)

filename = '/tmp/model'


def evaluate_next_batch(i):
    # Pin the process to a specific core if we are on Linux to prevent
    # contention between the different processes since TensorFlow uses
    # multiple threads.
    if sys.platform == 'linux':
        psutil.Process().cpu_affinity([i])
    model = tf.keras.models.load_model(filename)
    mnist = tf.keras.datasets.mnist.load_data()
    x_test = mnist[1][0] / 255.0
    return model.predict(x_test)


def main():
    # Time the code below.

    pool = Pool(num_cpus)

    for _ in range(10):
        pool.map(evaluate_next_batch, range(num_cpus))


if __name__ == '__main__':
    main()
