#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=bare-except

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import json
import requests
from bs4 import BeautifulSoup
from pandas import DataFrame as df

page = requests.get("https://www.familydollar.com/locations/")
soup = BeautifulSoup(page.text, 'html.parser')

# find all state links
state_list = soup.find_all(class_='itemlist')

state_links = []

for i in state_list:
    cont = i.contents[0]
    attr = cont.attrs
    hrefs = attr['href']
    state_links.append(hrefs)

# find all city links
city_links = []

for link in state_links:
    page = requests.get(link)
    soup = BeautifulSoup(page.text, 'html.parser')
    familydollar_list = soup.find_all(class_='itemlist')
    for store in familydollar_list:
        cont = store.contents[0]
        attr = cont.attrs
        city_hrefs = attr['href']
        city_links.append(city_hrefs)
# to get individual store links
store_links = []

for link in city_links:
    locpage = requests.get(link)
    locsoup = BeautifulSoup(locpage.text, 'html.parser')
    locinfo = locsoup.find_all(type="application/ld+json")
    for i in locinfo:
        loccont = i.contents[0]
        locjson = json.loads(loccont)
        try:
            store_url = locjson['url']
            store_links.append(store_url)
        except:
            pass

# get address and geolocation information
stores = []

for store in store_links:
    storepage = requests.get(store)
    storesoup = BeautifulSoup(storepage.text, 'html.parser')
    storeinfo = storesoup.find_all(type="application/ld+json")
    for i in storeinfo:
        storecont = i.contents[0]
        storejson = json.loads(storecont)
        try:
            store_addr = storejson['address']
            store_addr.update(storejson['geo'])
            stores.append(store_addr)
        except:
            pass

# final data parsing
stores_df = df.from_records(stores)
stores_df.drop(['@type', 'addressCountry'], axis=1, inplace=True)
stores_df['Store'] = "Family Dollar"

df.to_csv(stores_df, "family_dollar_locations.csv", sep=",", index=False)
