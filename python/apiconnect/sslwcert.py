#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import http.client
import ssl

# Defining certificate related stuff and host of endpoint

certificate_file = 'client.crt'
key_file = 'client.key'
host = 'prod.idrix.eu'

# Defining parts of the HTTP request
request_url = 'https://prod.idrix.eu/secure/'
request_headers = {'Content-Type': 'application/json'}

# Define the client certificate settings for https connection
context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.load_cert_chain(certfile=certificate_file, keyfile=key_file)

# Create a connection to submit HTTP requests
connection = http.client.HTTPSConnection(host, port=443, context=context)

# Use connection to submit a HTTP POST request
connection.request(method="GET", url=request_url, headers=request_headers)

# Print the HTTP response from the IOT service endpoint
response = connection.getresponse()
print(response.status, response.reason)
data = response.read()
print(data)
