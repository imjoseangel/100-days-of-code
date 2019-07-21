#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Generate Technical Debt Documentation'''

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
import argparse
import glob
import os
import re
import sys
import git

FALLBACK_ARGS = dict(file='technicaldebt.md', searchtext='TODO')


class TechnicalDebt():
    ''' Main Class. Parses arguments and generate file'''
    def __init__(self):

        # Parse arguments passed at cli
        self.parse_arguments()

        self.repo = git.Repo(search_parent_directories=True)
        self._work_path = self.repo.git.rev_parse("--show-toplevel")

        try:
            self.markdown = open(
                self._work_path + '/{0}/'.format(self.args.dir) +
                self.args.file, 'w')
        except FileNotFoundError:
            print('Unable to create file. Check if path exists')
            sys.exit(1)

        self.mainfunc()

        self.markdown.close()

        if self.args.stdout:
            try:
                markdown = open(
                    self._work_path + '/{0}/'.format(self.args.dir) +
                    self.args.file, 'r')
                for line in markdown:
                    print(line, end='')
            except FileNotFoundError:
                print('Unable to read file. Check if path exists')
                sys.exit(1)

    def includebyext(self):
        '''Add extension pattern'''
        files = [
            filename
            for filename in glob.glob(self._work_path +
                                      "/**/*{0}".format(self.args.include),
                                      recursive=True)
            if os.path.isfile(os.path.join(self._work_path, filename))
        ]
        return files

    def excludebyext(self):
        '''Remove extension pattern'''
        files = [
            filename
            for filename in glob.glob(self._work_path +
                                      "/**/*[!{0}]".format(self.args.exclude),
                                      recursive=True)
            if os.path.isfile(os.path.join(self._work_path, filename))
        ]
        return files

    def createmdheader(self):
        '''Generate Header for Technical Debt Document'''
        self.markdown.write('# Technical Debt Document\n\n')
        self.markdown.write(
            '## This document contains technical debt for project {0}\n\n'.
            format(os.path.basename(os.path.normpath(self._work_path))))

    def mainfunc(self):
        ''' Main Func'''
        if self.args.include:
            filestomanage = self.includebyext()
        elif self.args.exclude:
            filestomanage = self.excludebyext()

        self.createmdheader()
        for file in filestomanage:
            try:
                with open(file, 'r') as fileread:
                    filetitle = False
                    for num, line in enumerate(fileread, 1):
                        if self.args.text + ': ' in line and not filetitle:
                            self.markdown.write('### **{0}**\n\n'.format(
                                file.replace(self._work_path + '/', '')))
                            filetitle = True
                            self.markdown.write('(line {0}) : {1}\n'.format(
                                num,
                                re.sub(r'^.*' + self.args.text + r':\s', '',
                                       line)))
                        elif self.args.text + ': ' in line and filetitle:
                            self.markdown.write('(line {0}) : {1}\n'.format(
                                num,
                                re.sub(r'^.*' + self.args.text + r':\s', '',
                                       line)))
            except UnicodeDecodeError:
                pass

    def parse_arguments(self):
        '''argument parser'''
        parser = argparse.ArgumentParser(
            description='Create Technical Debt Document')
        parser.add_argument('--text',
                            '-t',
                            help='text to search for. default: "TODO"',
                            default=FALLBACK_ARGS['searchtext'])
        parser.add_argument(
            '--file',
            '-f',
            help='filename to write to. default: "technicaldebt.md"',
            default=FALLBACK_ARGS['file'])
        parser.add_argument('--stdout',
                            '-s',
                            help='print output to stdout',
                            action='store_true')
        parser.add_argument('--dir',
                            '-d',
                            help='path to store file. default: current',
                            default='')

        args_inexclude = parser.add_mutually_exclusive_group()
        args_inexclude.add_argument(
            '--exclude',
            '-e',
            help='exclude file extension. default: "none"',
            default=' ')
        args_inexclude.add_argument(
            '--include',
            '-i',
            help='include file extension. default: "all"',
            default='')

        self.args = parser.parse_args()


def main():
    '''main call'''
    TechnicalDebt()


if __name__ == '__main__':
    main()
