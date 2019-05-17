#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)
import time


# Everyone in queue, and their desired order
def get_customers():
    return [('Bob', 'Ham Sandwich'), ('Paul', 'Grilled Cheese'),
            ('Sally', 'Chicken Croissant')]


customers = get_customers()
print(customers)


# As people enter the queue, take their order, but pause(yield) to make their
# sandwich
def get_next_customer():
    # people are going to be adding themselves to this queue and it will grow
    # quickly
    list_of_customers = [('Bob', 'Ham Sandwich'), ('Paul', 'Grilled Cheese'),
                         ('Sally', 'Chicken Croissant')]
    for an_order in list_of_customers:
        yield an_order
        print(list(an_order))


# make the sandwiches for all the customers, then deliver
def old_make_sandwiches():
    completed_sandwiches = []
    for customer in customers:
        time.sleep(1)  # making the sandwich for our custoemr
        completed_sandwiches.append((customer[0], customer[1]))
    return completed_sandwiches


# make a sandwich, but pause(yield) to deliver it
def make_sandwiches():
    for customer in get_next_customer():
        time.sleep(1)  # making the sandwich for our customer
        yield (customer[0], customer[1])


sandwiches = make_sandwiches()


def make_sandwich(forcustomers):
    for customer in forcustomers:
        time.sleep(
            1)  # let's pretend this is the time it takes to make the sandwich
        yield customer


def make_nocustomer_sandwich():
    customer = yield 'No Customer'
    print(customer)


def employees():
    for y in ['Bob', 'Sally', 'Jake']:
        yield y


def newcustomers():
    for ex in ['James', 'Ted', 'Kent']:
        yield ex


def retrieve_all_users():
    yield from employees()
    yield from newcustomers()


def main():
    # deliver the sandwiches
    for sandwich in sandwiches:
        print('Delivering sandwich:', sandwich[1], 'for', sandwich[0])

    maker = make_sandwich(['Bob', 'Paul', 'Sally'])
    print('Just made a sandwich for:', next(maker))
    print('Just made a sandwich for:', next(maker))
    print('Just made a sandwich for:', next(maker))

    action = make_nocustomer_sandwich()
    print(next(action))
    try:
        print(action.send(13))
    except StopIteration:
        pass

    for user in retrieve_all_users():
        print(user)


if __name__ == '__main__':
    main()
