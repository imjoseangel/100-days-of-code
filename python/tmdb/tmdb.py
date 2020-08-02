#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import os
import requests

api_key = os.environ['TMDB_API']

response = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=' +
                        api_key + '&primary_release_year=2017&sort_by=revenue.desc')

print(response.json())


def main():
    pass


if __name__ == '__main__':
    main()
