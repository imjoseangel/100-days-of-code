#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=unused-argument

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import signal
import os
import time
import sys
import requests


def receiveSignal(signalNumber, frame):
    print('Received:', signalNumber)


def readConfiguration(signalNumber, frame):
    print(
        requests.get(
            "https://webhook.site/06f36d6a-4ba5-4a67-b355-3347e825831a",
            stream=True))


def terminateProcess(signalNumber, frame):
    print('(SIGTERM) terminating the process')
    sys.exit()


def main():
    # register the signals to be caught
    signal.signal(signal.SIGHUP, readConfiguration)
    signal.signal(signal.SIGINT, receiveSignal)
    signal.signal(signal.SIGQUIT, receiveSignal)
    signal.signal(signal.SIGILL, receiveSignal)
    signal.signal(signal.SIGTRAP, receiveSignal)
    signal.signal(signal.SIGABRT, receiveSignal)
    signal.signal(signal.SIGBUS, receiveSignal)
    signal.signal(signal.SIGFPE, receiveSignal)
    # signal.signal(signal.SIGKILL, receiveSignal)
    signal.signal(signal.SIGUSR1, receiveSignal)
    signal.signal(signal.SIGSEGV, receiveSignal)
    signal.signal(signal.SIGUSR2, receiveSignal)
    signal.signal(signal.SIGPIPE, receiveSignal)
    signal.signal(signal.SIGALRM, receiveSignal)
    signal.signal(signal.SIGTERM, readConfiguration)

    # output current process id
    print('My PID is:', os.getpid())

    # wait in an endless loop for signals
    while True:
        print('Waiting...')
        time.sleep(3)


if __name__ == '__main__':
    main()
