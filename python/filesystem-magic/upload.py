#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import os
import sys

from fs import open_fs

file_path = sys.argv[1]
fs_url = sys.argv[2]

filename = os.path.basename(file_path)

with open_fs(fs_url) as fs:
    if fs.exists(filename):
        print("destination exists! aborting.")
    else:
        with open(file_path, "rb") as bin_file:
            fs.upload(filename, bin_file)
print("upload successful!")
