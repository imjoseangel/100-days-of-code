#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Checks Pylint over all the python files found"""

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
import importlib
import os
import sys
import re
import subprocess

try:
    importlib.import_module('git')
    import git
except ImportError:
    print("GitPython is not installed")
    sys.exit(1)


class WorkPath:
    # WorkPath Class

    def __init__(self, branch):
        self._path = os.path.dirname(os.path.realpath(__file__))
        self._work_path = os.path.dirname(self._path)
        os.chdir(self._work_path)
        self.branch = branch

    def workpath(self):
        # Return Work Path
        return self._work_path

    def path(self):
        # Return Path
        return self._path

    def __gitdownload(self):

        self.workpath()
        repo = git.Repo()
        for item in repo.index.diff(self.branch):
            yield item.a_path

    def getchanges(self):

        changes = list(self.__gitdownload())
        return changes


def asterisks():
    # Calculate Screen Size

    rows, columns = os.popen('stty size', 'r').read().split()

    if rows:
        pass

    print('-' * int(columns))


def main():
    # Main Function

    # Sets default exit status code
    return_code = 0

    myproject = WorkPath('devel')
    project_changes = myproject.getchanges()
    work_path = myproject.workpath()

    for filename in project_changes:
        if filename.endswith('.py'):
            pythonfile = os.path.join(work_path, filename)

            print("Filename: {0}".format(pythonfile))
            asterisks()

            proc = subprocess.Popen('pylint %s' % pythonfile,
                                    shell=True,
                                    executable="/bin/bash",
                                    stdin=None,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            proc.wait()

            for line in iter(proc.stdout.readline, b''):

                score = re.search(r"(?P<score>\d?\d\.\d\d)",
                                  line.decode('UTF-8'))
                if score:
                    print(line.decode('UTF-8'))
                    rate = float(score.group('score'))
                else:
                    rate = float(10.0)

                if rate < 9.0:
                    return_code = 1

    sys.exit(return_code)


if __name__ == '__main__':
    main()
