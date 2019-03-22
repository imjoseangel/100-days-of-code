#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Socker Programming - Server"""

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mysocket:
    mysocket.bind((HOST, PORT))
    mysocket.listen()
    connection, address = mysocket.accept()
    print(connection, address)
    with connection:
        print('Connected by', address)
        while True:
            data = connection.recv(1024)
            if not data:
                break
            connection.sendall(data)
