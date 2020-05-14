#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from bcoding import bdecode


def main():
    with open('debian-live-10.3.0-amd64-gnome.iso.torrent', 'rb') as f:
        meta_info = f.read()
        torrent = bdecode(meta_info)
        print(torrent['info']['name'])


if __name__ == '__main__':
    main()
