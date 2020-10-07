#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
import json
import os
import requests

APIKEY = "&apikey=" + os.environ['OMDB_API']  # pragma: allowlist secret
MOVIETITLES = ['scream', 'terminator 2']
BASEURL = "http://omdbapi.com/?t="
MOVIES = list()


def main():

    for movie in MOVIETITLES:
        try:
            response = requests.get(BASEURL + movie + APIKEY)
            if response.status_code == 200:
                MOVIES.append(json.loads(response.text))
        except ValueError as error:
            print("Bad request! {0}".format(error))

    with open('movies.json', 'w') as filehandle:
        filehandle.writelines("%s\n" % movie for movie in MOVIES)


if __name__ == '__main__':
    main()
