#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import pymongo  # package for working with MongoDB


def mongo_connect(database, table):

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    database = client[database]
    table = database[table]

    return table


def mongo_exec(connection):

    customers_list = [{
        "name": "Amy",
        "address": "Apple st 652"
    }, {
        "name": "Hannah",
        "address": "Mountain 21"
    }, {
        "name": "Michael",
        "address": "Valley 345"
    }, {
        "name": "Sandy",
        "address": "Ocean blvd 2"
    }, {
        "name": "Betty",
        "address": "Green Grass 1"
    }, {
        "name": "Richard",
        "address": "Sky st 331"
    }, {
        "name": "Susan",
        "address": "One way 98"
    }, {
        "name": "Vicky",
        "address": "Yellow Garden 2"
    }, {
        "name": "Ben",
        "address": "Park Lane 38"
    }, {
        "name": "William",
        "address": "Central st 954"
    }, {
        "name": "Chuck",
        "address": "Main Road 989"
    }, {
        "name": "Viola",
        "address": "Sideway 1633"
    }]

    insert_customers = connection.insert_many(customers_list)
    return insert_customers.inserted_ids


def mongo_find(connect):

    for item in connect.find():
        yield item


def mongo_delete(connect):

    connect.drop()


def main():

    connect = mongo_connect("customersdb", "customers")
    insert_customers = mongo_exec(connect)
    print(insert_customers)

    customers = mongo_find(connect)

    for item in customers:
        print(item)

    mongo_delete(connect)


if __name__ == '__main__':
    main()
