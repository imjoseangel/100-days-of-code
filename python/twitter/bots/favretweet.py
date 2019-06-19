#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=arguments-differ,super-init-not-called

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
import logging
import tweepy
from config import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        logger.info("Processing tweet id %s", tweet.id)
        if tweet.in_reply_to_status_id is not None or \
                tweet.user.id == self.me.id:
            return
        try:
            tweet.favorite()
            tweet.retweet()
        except tweepy.TweepError:
            logger.error("Error on fav and retweet", exc_info=True)

    def on_error(self, status):
        logger.error(status)


def main(keywords):
    api = create_api()
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["en"])


if __name__ == '__main__':
    main(["Python", "Tweepy"])
