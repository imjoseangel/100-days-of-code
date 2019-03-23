#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Socker Programming - Multi Connection Server"""

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import sys
import socket
import selectors
import traceback

import libclient

sel = selectors.DefaultSelector()


def create_request(create_action, create_value):
    if action == "search":
        return dict(
            type="text/json",
            encoding="utf-8",
            content=dict(action=create_action, value=create_value),
        )
    else:
        return dict(
            type="binary/custom-client-binary-type",
            encoding="binary",
            content=bytes(action + value, encoding="utf-8"),
        )


def start_connection(start_host, start_port, start_request):
    addr = (start_host, start_port)
    print("starting connection to", addr)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.connect_ex(addr)
    start_events = selectors.EVENT_READ | selectors.EVENT_WRITE
    start_message = libclient.Message(sel, sock, addr, start_request)
    sel.register(sock, start_events, data=start_message)


if len(sys.argv) != 5:
    print("usage:", sys.argv[0], "<host> <port> <action> <value>")
    sys.exit(1)

host, port = sys.argv[1], int(sys.argv[2])
action, value = sys.argv[3], sys.argv[4]
request = create_request(action, value)
start_connection(host, port, request)

try:
    while True:
        events = sel.select(timeout=1)
        for key, mask in events:
            message = key.data
            try:
                message.process_events(mask)
            except socket.error as exception:
                print(
                    "main: error: exception for",
                    f"{message.addr}:\n{traceback.format_exc()}",
                )
                message.close()
        # Check for a socket being monitored to continue.
        if not sel.get_map():
            break
except KeyboardInterrupt:
    print("caught keyboard interrupt, exiting")
finally:
    sel.close()
