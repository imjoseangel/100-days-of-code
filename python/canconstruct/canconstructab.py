#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


def canConstruct(target: str, wordBank: list, memo: dict = None) -> bool:

    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]

    if target == "":
        return True

    for word in wordBank:
        try:
            if target.index(word) == 0:
                suffix = target[len(word):]
                if canConstruct(suffix, wordBank, memo) is True:
                    memo[target] = True
                    return True
        except ValueError:
            pass

    memo[target] = False
    return False


def main():
    print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # True
    print(canConstruct("skateboard", [
          "bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # False
    print(canConstruct("enterapotentpot", [
          "a", "p", "ent", "enter", "ot", "o", "t"]))  # True
    print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                       ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))  # False


if __name__ == '__main__':
    main()
