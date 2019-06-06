#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)
import os
import argparse

fallback_args = dict(basedir=os.path.dirname((os.path.realpath(__file__))))


class runupdate():
    def __init__(self):

        # Parse arguments passed at cli
        self.parse_arguments()

        for dirname in next(os.walk(self.args.basedir))[1]:
            print(dirname)

    def parse_arguments(self):
        parser = argparse.ArgumentParser(description='Update Git Repositories')
        parser.add_argument('--basedir',
                            '-b',
                            help='Base Directory to search in.',
                            default=fallback_args['basedir'])

        self.args = parser.parse_args()


def main():
    runupdate()


if __name__ == '__main__':
    main()
