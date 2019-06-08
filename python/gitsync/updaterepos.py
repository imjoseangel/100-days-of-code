#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)
import os
import argparse
import subprocess

fallback_args = dict(basedir=os.path.dirname((os.path.realpath(__file__))))


class runupdate():
    def __init__(self):

        self.commands = {
            "remote prunte origin": "Pruning branches for {0}",
            "pull origin develop": "Pulling new code on {0}",
            "fetch -t": "Updating tags for {0}"
        }

        # Parse arguments passed at cli
        self.parse_arguments()

        # Update Git Directories
        self.update_git()

    @staticmethod
    def get_directories(directory):
        return next(os.walk(directory))[1]

    def update_git(self):
        for command in self.commands:
            print(self.commands[command])

        directories = self.get_directories(self.args.basedir)
        for directory in directories:
            dir_fullpath = self.args.basedir + '/' + directory
            subdirs = self.get_directories(dir_fullpath)
            if '.git' in subdirs:
                proc = subprocess.Popen("git remote prune origin",
                                        shell=True,
                                        executable="/bin/bash",
                                        cwd=dir_fullpath,
                                        stdin=None,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.STDOUT)
                proc.wait()
                print("Pruning branches for {0}".format(directory))

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
