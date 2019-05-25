#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=no-self-use, C0330

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)
import scrapy


class RedditSpider(scrapy.Spider):
    name = 'reddit'
    start_urls = ['https://www.reddit.com']

    def parse(self, response):
        links = response.xpath('//a/@href')
        html = ''
        for link in links:
            # Extract the URL text from the element
            url = link.get()
            # Check if the URL contains an image extension
            if any(extension in url
                   for extension in ['.jpg', '.gif', '.png']) and not any(
                       domain in url
                       for domain in ['redditstatic.com', 'redditmedia.com']):
                html += '''
                <a href="{url}" target="_blank">
                    <img src="{url}" height="33%" width="33%" />
                </a>
                '''.format(url=url)

                # Open an HTML file, save the results
                with open('frontpage.html', 'a') as page:
                    page.write(html)
                # Close the file
                page.close()
