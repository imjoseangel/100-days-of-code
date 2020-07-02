#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import argparse
import logging
import sys
import requests


class DuckDNS():
    def __init__(self):

        # Parse arguments passed at cli
        self.parse_arguments()
        logging.basicConfig(format="%(asctime)s - %(message)s",
                            datefmt="%d-%b-%y %H:%M:%S", stream=sys.stdout, level=logging.INFO)
        self.req = ""
        self.mainfunc()

    def parse_arguments(self):
        '''argument parser'''
        parser = argparse.ArgumentParser(
            description='Update DuckDNS.org')

        args_required = parser.add_argument_group('Required named arguments')
        args_required.add_argument('--domain',
                                   '-d',
                                   help='Single domain to update', required=True)
        args_required.add_argument(
            '--token',
            '-t',
            help='User token', required=True)

        self.args = parser.parse_args()

    def duckdns(self, domain, token):
        try:
            self.req = requests.get(
                "https://www.duckdns.org/update?domains={0}&token={1}&ip=".format(domain, token))

            return self.req.content

        except requests.RequestException as exception:
            logging.error(exception)

    def mainfunc(self):

        self.runduckdns = self.duckdns(self.args.domain, self.args.token)

        if self.runduckdns is not None:
            logging.info(self.runduckdns.decode())


def main():
    DuckDNS()


if __name__ == '__main__':
    main()
