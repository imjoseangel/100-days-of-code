#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)
from collections import defaultdict
from multiprocessing import Pool
import numpy as np
import psutil

num_cpus = psutil.cpu_count(logical=False)


def accumulate_prefixes(args):
    running_prefix_count, running_popular_prefixes, document = args
    for word in document:
        for i in range(1, len(word)):
            prefix = word[:i]
            running_prefix_count[prefix] += 1
            if running_prefix_count[prefix] > 3:
                running_popular_prefixes.add(prefix)
    return running_prefix_count, running_popular_prefixes


def main():
    # Time the code below.

    pool = Pool(num_cpus)

    running_prefix_counts = [defaultdict(int) for _ in range(4)]
    running_popular_prefixes = [set() for _ in range(4)]

    for _ in range(10):
        documents = [[np.random.bytes(20) for _ in range(10000)]
                     for _ in range(num_cpus)]
        results = pool.map(
            accumulate_prefixes,
            zip(running_prefix_counts, running_popular_prefixes, documents))
        running_prefix_counts = [result[0] for result in results]
        running_popular_prefixes = [result[1] for result in results]

    popular_prefixes = set()
    for prefixes in running_popular_prefixes:
        popular_prefixes |= prefixes


if __name__ == '__main__':
    main()
