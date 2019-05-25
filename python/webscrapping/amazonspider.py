#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=no-self-use

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)

from re import sub
from decimal import Decimal
import scrapy


def convert_money(money):
    return Decimal(sub(r'[^\d.]', '', money))


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = ['https://www.amazon.com/s?k=paint']

    def parse(self, response):
        # Find the Amazon price element
        prices = response.css('.a-price .a-offscreen::text').getall()

        # Initialize some counters and stats objects
        stats = dict()
        values = []

        for price in prices:
            value = convert_money(price)
            values.append(value)

        # Sort our values before calculating
        values.sort()

        # Calculate price statistics
        stats['average_price'] = round(sum(values) / len(values), 2)
        stats['lowest_price'] = values[0]
        stats['highest_price'] = values[-1]
        stats['total_prices'] = len(values)

        print(stats)
