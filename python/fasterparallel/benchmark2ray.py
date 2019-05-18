#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)
from collections import defaultdict
import numpy as np
import psutil
import ray

num_cpus = psutil.cpu_count(logical=False)

ray.init(num_cpus=num_cpus)


@ray.remote
class StreamingPrefixCount():
    def __init__(self):
        self.prefix_count = defaultdict(int)
        self.popular_prefixes = set()

    def add_document(self, document):
        for word in document:
            for i in range(1, len(word)):
                prefix = word[:i]
                self.prefix_count[prefix] += 1
                if self.prefix_count[prefix] > 3:
                    self.popular_prefixes.add(prefix)

    def get_popular(self):
        return self.popular_prefixes


streaming_actors = [StreamingPrefixCount.remote() for _ in range(num_cpus)]

filters = [np.random.normal(size=(4, 4)) for _ in range(num_cpus)]


def main():
    # Time the code below.

    for i in range(num_cpus * 10):
        document = [np.random.bytes(20) for _ in range(10000)]
        streaming_actors[i % num_cpus].add_document.remote(document)

    # Aggregate all of the results.
    results = ray.get(
        [actor.get_popular.remote() for actor in streaming_actors])
    popular_prefixes = set()
    for prefixes in results:
        popular_prefixes |= prefixes


if __name__ == '__main__':
    main()
