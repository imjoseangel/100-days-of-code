#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=unused-variable

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import concurrent.futures
import logging
import queue
import random
import threading
import time


def producer(queueprod, eventprod):
    """Pretend we're getting a number from the network."""
    while not eventprod.is_set():
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        queueprod.put(message)

    logging.info("Producer received event. Exiting")


def consumer(queuecons, eventcons):
    """Pretend we're saving a number in the database."""
    while not eventcons.is_set() or not queuecons.empty():
        message = queuecons.get()
        logging.info("Consumer storing message: %s (size=%d)", message,
                     queuecons.qsize())

    logging.info("Consumer received event. Exiting")


if __name__ == "__main__":
    formatmsg = "%(asctime)s: %(message)s"
    logging.basicConfig(
        format=formatmsg, level=logging.INFO, datefmt="%H:%M:%S")

    pipeline = queue.Queue(maxsize=10)
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(0.1)
        logging.info("Main: about to set event")
        event.set()
