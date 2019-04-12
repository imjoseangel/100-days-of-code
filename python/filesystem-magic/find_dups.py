#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from collections import defaultdict
import hashlib
import sys

from fs import open_fs


def get_hash(getbin_file):
    """Get the md5 hash of a file."""
    getfile_hash = hashlib.md5()
    while True:
        chunk = getbin_file.read(1024 * 1024)
        if not chunk:
            break
        getfile_hash.update(chunk)
    return getfile_hash.hexdigest()


hashes = defaultdict(list)
with open_fs(sys.argv[1]) as fs:
    for path in fs.walk.files():
        with fs.open(path, "rb") as bin_file:
            file_hash = get_hash(bin_file)
        hashes[file_hash].append(path)

for paths in hashes.values():
    if len(paths) > 1:
        for path in paths:
            print(f" {path}")
        print()
