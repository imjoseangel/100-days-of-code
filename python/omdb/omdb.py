#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
import json
import os
import requests

APIKEY = "&apikey=" + os.environ['OMDB_API']  # pragma: allowlist secret
MOVIES = ['scream', 'terminator 2']
BASEURL = "http://omdbapi.com/?t="


def main():

    for movieTitle in MOVIES:
        response = requests.get(BASEURL + movieTitle + APIKEY)
        if response.status_code == 200:
            movie = json.loads(response.text)
            print(movie)
        else:
            raise ValueError("Bad request!")


if __name__ == '__main__':
    main()
