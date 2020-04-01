#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import os
import argparse
import base64
import requests


class odnsupdate():
    def __init__(self):

        self.fallback_args = dict(hostname='home', username='', password='')

        # Parse arguments passed at cli
        self.parse_arguments()

        self.url = 'https://updates.opendns.com/nic/update?hostname={0}'.format(
            self.args.hostname)

        # Generate Base64 Auth
        self.authencode()

        # Update Git Directories
        self.update_opendns()

    @staticmethod
    def asterisks(title):

        _, columns = os.popen('stty size', 'r').read().split()
        print('[{0}]'.format(title),
              '*' * (int(columns) - int(len(title)) - 3) + '\n')

    def authencode(self):

        self.auth = '{0}:{1}'.format(self.args.username, self.args.password)
        self.encodeauth = base64.b64encode(self.auth.encode('utf-8'))

        self.headers = {
            'Authorization':
            'Basic {0}'.format(self.encodeauth.decode('utf-8'))
        }

    def update_opendns(self):

        self.asterisks(self.url)

        try:
            self.response = requests.request(
                'GET', self.url, headers=self.headers).content.decode('utf-8')

        except requests.exceptions.ConnectionError as e:
            print('Connection error to URI: {0} \n\nException: {1}'.format(
                self.url, repr(e)))

    def parse_arguments(self):
        parser = argparse.ArgumentParser(description='Update OpenDNS IP')
        parser.add_argument('--hostname',
                            '-t',
                            help='OpenDNS hostname',
                            default=self.fallback_args['hostname'])
        parser.add_argument('--username',
                            '-u',
                            help='OpenDNS username',
                            default=self.fallback_args['username'])
        parser.add_argument('--password',
                            '-p',
                            help='OpenDNS password',
                            default=self.fallback_args['password'])

        self.args = parser.parse_args()


def main():
    opendns = odnsupdate()
    print(opendns.response)


if __name__ == '__main__':
    main()
