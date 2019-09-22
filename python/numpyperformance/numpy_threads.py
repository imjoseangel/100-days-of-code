import cProfile
import io
import logging

from time import time

import pstats
from threading import Thread
import queue

import numpy as np

q = queue.Queue()

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(filename)s - %(message)s',
    level=logging.INFO)

pr = cProfile.Profile()


# @jit(parallel=True)
def test_sinc(array_size):
    x = np.linspace(-4, 4, array_size)
    return np.sinc(x)


n = 50
array = 200000
pr.enable()
t = time()

# processes = [
#     mp.Process(target=test_sinc, args=(array_size, )) for _ in range(n)
# ]

# for p in processes:
#     p.start()
# for p in processes:
#     p.join()

# pool = mp.Pool(processes=2)

# [pool.apply(test_sinc, (array_size, )) for _ in range(n)]

threads = [Thread(target=test_sinc, args=(array, )) for _ in range(n)]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

delta = time() - t
pr.disable()

logging.info(delta / n)

s = io.StringIO()
ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
ps.print_stats()

for linenumber, line in enumerate(s.getvalue().split('\n')):
    if linenumber < 1:
        logging.info(line)

# logging.info(s.getvalue())

if __name__ == '__main__':
    pass
