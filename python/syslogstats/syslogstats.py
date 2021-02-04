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
        '''Main Function'''

        # Open File
        try:
            syslogfile = open('syslog', 'r')
        except FileNotFoundError as fileerror:
            logging.error(f"{fileerror}")
            sys.exit(1)

        # Prepare Regex Groups
        self.regex = re.compile(
            r"^((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s{1,2}\d{1,2})"
            r"\s\d{2}:\d{2}:\d{2}\s\S{1,256}\s(\w{1,256})")

        # Read File
        self.fileread = syslogfile.readlines()

        # Go to specific method depending on args
        if self.args.minute:
            self.application()
        else:
            self.events()

    def application(self):
        '''Application Function'''

        # Get group3 (Apps from regex when reading every line using list comprehension)
        getapps = [item.group(3)
                   for line in self.fileread if (item := self.regex.search(line))]

        # Use counter to count the apps
        numberofapps = (Counter(getapps)).items()

        # Output results
        for app in numberofapps:
            logging.info(f"App: {app[0]} - No. Events: {app[1]}")

    def events(self):

        # Get group1 (Month and Day from regex when reading every line using list comprehension)
        getdays = [item.group(1)
                   for line in self.fileread if (item := self.regex.search(line))]

        # Get number of days counter

        numberofdays = (Counter(getdays)).values()

        # Number of lines by the number of 24-hour periods
        # the file contains divided by 24 * 60 (Minutes)
        eventsbydate = (sum(numberofdays) / len(numberofdays)) / 1440

        # Output results
        logging.info(f"Events per minute: {eventsbydate:.4f}")


def main():
    '''main call'''
    SyslogStats()


if __name__ == '__main__':
    main()
