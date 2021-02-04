#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=W1203

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import argparse
import logging
import re
import sys
from collections import Counter


class SyslogStats():

    def __init__(self):

        # Parse arguments passed at cli
        self.parse_arguments()

        # Configure Logging
        logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s",
                            datefmt="%d-%b-%y %H:%M:%S", stream=sys.stdout, level=logging.INFO)

        self.mainfunc()

    def parse_arguments(self):
        '''argument parser'''
        parser = argparse.ArgumentParser(
            description='Read Syslog file')
        args_inexclude = parser.add_mutually_exclusive_group()
        args_inexclude.add_argument(
            '--minute',
            '-m',
            help='show events per minute',
            action='store_true')
        args_inexclude.add_argument(
            '--app',
            '-a',
            help='show events per application',
            action='store_true')

        self.args = parser.parse_args()

        if not (self.args.minute or self.args.app):
            parser.error('No arguments provided.')

    def mainfunc(self):

        try:
            syslogfile = open('syslog', 'r')
        except FileNotFoundError as fileerror:
            logging.error(f"{fileerror}")
            sys.exit(1)

        self.regex = re.compile(
            r"^((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s{1,2}\d{1,2})"
            r"\s\d{2}:\d{2}:\d{2}\s\S{1,256}\s(\w{1,256})")

        self.fileread = syslogfile.readlines()

        if self.args.minute:
            self.application()
        else:
            self.events()

    def application(self):
        getapps = [item.group(3)
                   for line in self.fileread if (item := self.regex.search(line))]
        numberofapps = (Counter(getapps)).items()

        for app in numberofapps:
            logging.info(f"App: {app[0]} - No. Events: {app[1]}")

    def events(self):
        getdays = [item.group(1)
                   for line in self.fileread if (item := self.regex.search(line))]

        numberofdays = (Counter(getdays)).values()
        # Number of lines by the number of 24-hour periods
        # the file contains divided by 24 * 60 (Minutes)
        eventsbydate = (sum(numberofdays) / len(numberofdays)) / 1440

        logging.info(f"Events per minute: {eventsbydate:.4f}")


def main():
    '''main call'''
    SyslogStats()


if __name__ == '__main__':
    main()
