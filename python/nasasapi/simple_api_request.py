#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)

from urllib.parse import urlencode, quote_plus
import requests


def main():
    base_url = 'https://images-api.nasa.gov/search'

    search_term = 'apollo 11'
    desc = 'moon landing'
    media = 'image'
    query = {'q': search_term, 'description': desc, 'media_type': media}
    full_url = base_url + '?' + urlencode(query, quote_via=quote_plus)

    r = requests.get(full_url)
    data = r.json()
    item = data['collection']['items'][0]

    nasa_id = item['data'][0]['nasa_id']
    asset_url = 'https://images-api.nasa.gov/asset/' + nasa_id
    image_request = requests.get(asset_url)
    image_json = image_request.json()
    image_urls = [url['href'] for url in image_json['collection']['items']]
    print(image_urls)


if __name__ == '__main__':
    main()
