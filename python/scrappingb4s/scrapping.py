#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=too-many-locals

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import json
import requests
from bs4 import BeautifulSoup
from pandas import DataFrame as df

URL = "https://locations.familydollar.com/id/"
HEADERS = {
    "User-Agent":
    "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
}


def main():

    page = requests.get(URL, headers=HEADERS)
    page.encoding = "ISO-885901"
    soup = BeautifulSoup(page.text, "html.parser")
    # print(soup.prettify())

    # dollar_tree_list = soup.find_all("href")

    dollar_tree_list = soup.find_all(class_="itemlist")
    # for item in dollar_tree_list[:2]:
    # print(item)

    # print(type(dollar_tree_list))
    # print(len(dollar_tree_list))

    # example = dollar_tree_list[2]  # a representative example
    # example_content = example.contents
    # print(example_content)

    # example_content = example.contents[0]
    # print(example_content.attrs)

    # example_href = example_content['href']
    # print(example_href)

    city_hrefs = list()  # initialise empty list

    for item in dollar_tree_list:
        contents = item.contents[0]
        href = contents['href']
        city_hrefs.append(href)

    #  check to be sure all went well showing the first 2 elements
    # for href in city_hrefs[:2]:
    # print(href)

    # page2 = requests.get(city_hrefs[2])  # again establish a representative example
    # soup2 = BeautifulSoup(page2.text, 'html.parser')
    # arco = soup2.find_all(type="application/ld+json")

    # print(arco[1])

    # arco_contents = arco[1].contents[0]
    # print(arco_contents)

    # arco_json = json.loads(arco_contents)

    # type(arco_json)
    # print(arco_json)

    # arco_address = arco_json['address']

    locs_dict = list()

    for link in city_hrefs:
        locpage = requests.get(link)  # request page info
        locsoup = BeautifulSoup(locpage.text, 'html.parser')
        # parse the page's content
        locinfo = locsoup.find_all(type="application/ld+json")
        # extract specific element
        loccont = locinfo[1].contents[0]
        # get contents from the bs4 element set
        locjson = json.loads(loccont)  # convert to json
        locaddr = locjson['address']  # get address
        locs_dict.append(locaddr)  # add address to list

    locs_df = df.from_records(locs_dict)
    # print(locs_df)

    locs_df.drop(['@type', 'addressCountry'], axis=1, inplace=True)
    locs_df.head(n=5)

    # save results
    df.to_csv(locs_df, "family_dollar_ID_locations.csv", sep=",", index=False)


if __name__ == '__main__':
    main()
