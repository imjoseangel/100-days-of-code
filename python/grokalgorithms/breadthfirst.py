#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function)
from collections import deque


def person_is_seller(name):
    return name[-1] == 'm'


def search(graph, name):
    search_queue = deque()
    search_queue += graph[name]
    searched = list()

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print("{0} is a mango seller!".format(person))
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


def main():

    graph = dict()
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = graph["peggy"] = graph["thom"] = graph["jonny"] = []

    search(graph, "you")


if __name__ == '__main__':
    main()
