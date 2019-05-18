#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)
from multiprocessing import Pool
import numpy as np
import psutil
import scipy.signal

num_cpus = psutil.cpu_count(logical=False)


def f(args):
    image, random_filter = args
    # Do some image processing.
    return scipy.signal.convolve2d(image, random_filter)[::5, ::5]


def main():
    # Time the code below.

    pool = Pool(num_cpus)

    filters = [np.random.normal(size=(4, 4)) for _ in range(num_cpus)]

    for _ in range(10):
        image = np.zeros((3000, 3000))
        pool.map(f, zip(num_cpus * [image], filters))


if __name__ == '__main__':
    main()
