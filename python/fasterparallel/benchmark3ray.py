#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)
import sys
import psutil
import ray
import tensorflow as tf

num_cpus = psutil.cpu_count(logical=False)

ray.init(num_cpus=num_cpus)

filename = '/tmp/model'


@ray.remote
class Model():
    def __init__(self, i):
        # Pin the actor to a specific core if we are on Linux to prevent
        # contention between the different actors since TensorFlow uses
        # multiple threads.
        if sys.platform == 'linux':
            psutil.Process().cpu_affinity([i])
        # Load the model and some data.
        self.model = tf.keras.models.load_model(filename)
        mnist = tf.keras.datasets.mnist.load_data()
        self.x_test = mnist[1][0] / 255.0

    def evaluate_next_batch(self):
        # Note that we reuse the same data over and over, but in a
        # real application, the data would be different each time.
        return self.model.predict(self.x_test)


actors = [Model.remote(i) for i in range(num_cpus)]


def main():
    # Time the code below.

    # Parallelize the evaluation of some test data.
    for _ in range(10):
        results = ray.get(
            [actor.evaluate_next_batch.remote() for actor in actors])
        print(results)


if __name__ == '__main__':
    main()
