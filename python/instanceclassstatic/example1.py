#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)


class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


def main():
    obj = MyClass()
    print(obj.method())
    print(MyClass.method(obj))
    print(obj.classmethod())
    print(obj.staticmethod())
    print(MyClass.classmethod())
    print(MyClass.staticmethod())
    # print(MyClass.method())
    # TypeError: method() missing 1 required positional argument: 'self'


if __name__ == '__main__':
    main()
