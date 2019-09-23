import cProfile
import io
import logging

import itertools
from time import time

import pstats
import numpy as np

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(filename)s - %(message)s',
    level=logging.INFO)

pr = cProfile.Profile()


def test_sinc(array_size):
    x = np.linspace(-4, 4, array_size)
    return np.sinc(x)


n = 50
array = 200000
pr.enable()
t = time()
for _ in itertools.repeat(None, n):
    test_sinc(array)
delta = time() - t
pr.disable()

logging.info(delta / n)

s = io.StringIO()
ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
ps.print_stats()
logging.info(s.getvalue())

if __name__ == '__main__':
    pass
