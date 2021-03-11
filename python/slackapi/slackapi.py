#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from time import sleep
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


CHANNEL = ""
MESSAGES_PER_PAGE = 200
MAX_MESSAGES = 1000
SLACK_TOKEN = ""
USERID = ""

# init web client
client = WebClient(token=SLACK_TOKEN)

# get first page

page = 1

response = client.conversations_history(
    channel=CHANNEL, limit=MESSAGES_PER_PAGE)

assert response['ok']
messages_all = response['messages']

for message in messages_all:
    if message['user'] == USERID:
        print(message)
        sleep(1)
        try:
            client.chat_delete(channel=CHANNEL, ts=message['ts'])
        except SlackApiError:
            pass

while len(messages_all) + MESSAGES_PER_PAGE <= MAX_MESSAGES and response['has_more']:
    page += 1

    response = client.conversations_history(
        channel=CHANNEL,
        limit=MESSAGES_PER_PAGE,
        cursor=response['response_metadata']['next_cursor']
    )
    assert response["ok"]
    messages = response['messages']
    messages_all = messages_all + messages

    for message in messages_all:
        if message['user'] == USERID:
            print(message)
            sleep(1)
            try:
                client.chat_delete(channel=CHANNEL, ts=message['ts'])
            except SlackApiError:
                pass
