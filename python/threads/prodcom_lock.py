#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=unused-variable

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import logging
import random
import concurrent.futures
import threading

SENTINEL = object()


class Pipeline:
    """
    Class to allow a single element pipeline between producer and consumer.
    """

    def __init__(self):
        self.message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()

    def get_message(self, name):
        logging.debug("%s:about to acquire getlock", name)
        self.consumer_lock.acquire()
        logging.debug("%s:have getlock", name)
        message = self.message
        logging.debug("%s:about to release setlock", name)
        self.producer_lock.release()
        logging.debug("%s:setlock released", name)
        return message

    def set_message(self, message, name):
        logging.debug("%s:about to acquire setlock", name)
        self.producer_lock.acquire()
        logging.debug("%s:have setlock", name)
        self.message = message
        logging.debug("%s:about to release getlock", name)
        self.consumer_lock.release()
        logging.debug("%s:getlock released", name)


def producer(pipelineprod):
    """Pretend we're getting a message from the network."""
    for index in range(10):
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        pipeline.set_message(message, "Producer")

    # Send a sentinel message to tell consumer we're done
    pipelineprod.set_message(SENTINEL, "Producer")


def consumer(pipelinecons):
    """Pretend we're saving a number in the database."""
    message = 0
    while message is not SENTINEL:
        message = pipelinecons.get_message("Consumer")
        if message is not SENTINEL:
            logging.info("Consumer storing message: %s", message)


if __name__ == "__main__":
    formatmsg = "%(asctime)s: %(message)s"
    logging.basicConfig(
        format=formatmsg, level=logging.INFO, datefmt="%H:%M:%S")
    # logging.getLogger().setLevel(logging.DEBUG)

    pipeline = Pipeline()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline)
        executor.submit(consumer, pipeline)
