#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Checks Linters over all the ansible files found"""

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
import importlib
import os
import sys
import subprocess
import configparser
import ast
import re

try:
    importlib.import_module('git')
    import git
except ImportError:
    print("GitPython is not installed")
    sys.exit(1)


class WorkPath:
    """ WorkPath Class """

    def __init__(self):
        self._path = os.path.dirname(os.path.realpath(__file__))
        self._work_path = os.path.dirname(self._path)
        os.chdir(self._work_path)
        self._config = configparser.ConfigParser()
        self._config.read(self._path + '/{0}'.format('lint_checker.ini'))
        if 'branch' in self._config['DEFAULT']:
            self.branch = self._config['DEFAULT']['branch']
        else:
            self.branch = 'devel'

    def workpath(self):
        """ Return Work Path """
        return self._work_path

    def path(self):
        """ Returns Path """
        return self._path

    def config(self):
        """ Returns Path """
        return self._config

    def __gitdownload(self):

        self.workpath()
        repo = git.Repo()
        repo.git.remote('set-branches', 'origin', self.branch)
        for remote in repo.remotes:
            remote.fetch()
        for item in repo.index.diff('origin/{0}'.format(self.branch)):
            if item.a_blob is not None:
                yield item.a_path

    def getchanges(self):
        """ Returns Git Changes """

        changes = list(self.__gitdownload())
        return changes


def asterisks():
    """ Show Line """

    print('=' * int(78))


def runlinter(binary, args, file):
    """ Run Specific Linter """
    try:

        lint_proc = subprocess.Popen(binary + ' ' + args + ' {0}'.format(file),
                                     shell=True,
                                     executable="/bin/bash",
                                     stdin=None,
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT)
        lint_proc.wait()

        return lint_proc

    except subprocess.CalledProcessError as exception:
        print(exception.output)
        sys.exit(1)


def getruninfo(runprocess, score):
    """ Get Return Code for the Process """
    runinfo_rc = 0

    for line in iter(runprocess.stdout.readline, b''):
        if score:
            linter_score = re.search(r"(?P<score>\d?\d\.\d\d)",
                                     line.decode('UTF-8'))
            if linter_score:
                print(line.decode('UTF-8'))
                rate = float(linter_score.group('score'))
            else:
                rate = float(10.0)

            if rate < 9.0:
                runinfo_rc = 1

        else:
            print(line.decode('UTF-8'))

            if runprocess.returncode > 0:
                runinfo_rc = 1

    return runinfo_rc


def main():
    """ Main Function """

    # Sets default exit status code
    return_code = 0

    myproject = WorkPath()
    project_changes = myproject.getchanges()
    work_path = myproject.workpath()
    config_file = myproject.config()
    config_sections = config_file.sections()

    for filename in project_changes:
        for section in config_sections:
            try:
                extensions = ast.literal_eval(config_file.get(
                    section, "files"))
            except ValueError:
                print('Error reading extensions, please be sure it is a list')
            if filename.endswith(tuple(extensions)):
                file = os.path.join(work_path, filename)

                print("Filename: {0}".format(file))
                asterisks()

                try:
                    binary = config_file[section]['binary']
                except KeyError:
                    print(
                        'Cannot read binary section, please be sure it exists')

                try:
                    args = config_file[section]['args']
                except KeyError:
                    args = ''

                try:
                    score = config_file[section]['score']
                except KeyError:
                    score = None

                run_linter = runlinter(binary, args, file)
                lintruninfo = getruninfo(run_linter, score)

                if lintruninfo == 1:
                    return_code = 1

    sys.exit(return_code)


if __name__ == '__main__':
    main()
