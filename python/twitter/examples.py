#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=arguments-differ,super-init-not-called

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import ast
import os
import tweepy


class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")

    def on_error(self, status):
        print(f"Error detected: {status}")


def asterisks(title):

    _, columns = os.popen('stty size', 'r').read().split()
    print('[{0}]'.format(title),
          '*' * (int(columns) - int(len(title)) - 3) + '\n')


def main():

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler("", "")

    auth.set_access_token("", "")

    # Create API object
    api = tweepy.API(auth,
                     wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    try:

        asterisks("Authentication")

        api.verify_credentials()
        print("Authentication OK\n")

    except tweepy.TweepError as e:

        print(list(ast.literal_eval(e.__dict__['reason']))[0]['message'])

    asterisks("Timeline")

    timeline = api.home_timeline()

    for tweet in timeline:
        print(f"{tweet.user.name} said {tweet.text}")
    print("\n")

    # # Create a tweet
    # api.update_status("Hello Tweepy")

    # Get User Data
    asterisks("Get User Data")
    user = api.get_user("commandlinefu")

    print("User details:")
    print(user.name)
    print(user.description)
    print(user.location)
    print("\n")

    asterisks("Last 20 Followers")
    for follower in user.followers():
        print(follower.name)
    print("\n")

    # # Follow RealPython
    # api.create_friendship("realpython")

    # # Update Profile Description
    # api.update_profile(description="I like Python")

    # # Mark as Liked first tweet in timeline
    # tweets = api.home_timeline(count=1)
    # tweet = tweets[0]
    # print(f"Liking tweet {tweet.id} of {tweet.author.name}")
    # api.create_favorite(tweet.id)

    # Blocked Users
    asterisks("Blocked Users")
    for block in api.blocks():
        print(block.name)
    print("\n")

    # Search
    asterisks("Search for Python Keyword")
    for tweet in api.search(q="Python", lang="en", rpp=10):
        print(f"{tweet.user.name}:{tweet.text}")
    print("\n")

    # Trends
    asterisks("Trends")
    trends_result = api.trends_place(1)
    for trend in trends_result[0]["trends"]:
        print(trend["name"])
    print("\n")

    # Cursors
    asterisks("Cursors")
    for tweet in tweepy.Cursor(api.home_timeline).items(100):
        print(f"{tweet.user.name} said: {tweet.text}")
    print("\n")

    # Streaming
    asterisks("Streaming")
    tweets_listener = MyStreamListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=["Python", "Django", "Tweepy", "thorne"],
                  languages=["en"])

    # # Follow and Favorite
    # tweets = api.mentions_timeline()
    # for tweet in tweets:
    #     tweet.favorite()
    #     tweet.user.follow()


if __name__ == '__main__':
    main()
