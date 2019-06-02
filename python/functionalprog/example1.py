#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)


def remove_last_item(mylist):
    """Removes the last item from a list."""
    mylist.pop(-1)  # This modifies mylist


def butlast(mylist):
    """Like butlast in Lisp; returns the list without the last element."""
    return mylist[:-1]  # This returns a copy of mylist


def main():

    # with map()
    map(lambda x: x + "bzz!", ["I think", "I'm good"])
    list(map(lambda x: x + "bzz!", ["I think", "I'm good"]))
    # ['I thinkbzz!', "I'm goodbzz!"]

    # map() equivalent
    mapequivalent = (x + "bzz!" for x in ["I think", "I'm good"])
    mapequivalentlist = [x + "bzz!" for x in ["I think", "I'm good"]]
    print(mapequivalent, mapequivalentlist)
    # ['I thinkbzz!', "I'm goodbzz!"]

    # with filter()
    filter(lambda x: x.startswith("I "), ["I think", "I'm good"])
    list(filter(lambda x: x.startswith("I "), ["I think", "I'm good"]))
    # ['I think']

    # filter() equivalent
    filterequivalent = (x for x in ["I think", "I'm good"]
                        if x.startswith("I "))
    filterequivalentlist = [
        x for x in ["I think", "I'm good"] if x.startswith("I ")
    ]
    print(filterequivalent, filterequivalentlist)
    # ['I think']

    # with enumerate()
    mylist = [1, 2, 3, 4, 5]
    i = 0

    while i < len(mylist):
        print("Item %d: %s" % (i, mylist[i]))
        i += 1

    # more efficient with enumerate()
    for i, item in enumerate(mylist):
        print("Item %d: %s" % (i, item))

    # sorted list with sorted()
    sorted([("a", 2), ("c", 1), ("d", 4)])
    # [('a', 2), ('c', 1), ('d', 4)]
    sorted([("a", 2), ("c", 1), ("d", 4)], key=lambda x: x[1])
    # [('c', 1), ('a', 2), ('d', 4)]

    # any and all (Check out functions above)

    # def all(iterable):
    #     for x in iterable:
    #         if not x:
    #             return False
    #     return True

    # def any(iterable):
    #     for x in iterable:
    #         if x:
    #             return True
    #     return False

    mylist = [0, 1, 3, -1]
    if all(map(lambda x: x > 0, mylist)):
        print("All items are greater than 0")
    if any(map(lambda x: x > 0, mylist)):
        print("At least one item is greater than 0")

    # zip()
    keys = ["foobar", "barzz", "ba!"]
    map(len, keys)
    zip(keys, map(len, keys))
    list(zip(keys, map(len, keys)))
    # [('foobar', 6), ('barzz', 5), ('ba!', 3)]
    dict(zip(keys, map(len, keys)))
    # {'foobar': 6, 'barzz': 5, 'ba!': 3}


if __name__ == '__main__':
    main()
