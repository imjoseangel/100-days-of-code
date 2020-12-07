#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


def countConstruct(target: str, wordBank: list, memo: dict = None) -> bool:

    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]

    if target == "":
        return 1

    totalCount = 0

    for word in wordBank:
        try:
            if target.index(word) == 0:
                numWaysForRest = countConstruct(
                    target[len(word):], wordBank, memo)
                totalCount += numWaysForRest
        except ValueError:
            pass

    memo[target] = totalCount
    return totalCount


def main():
    print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))  # 2
    print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # 1
    print(countConstruct("skateboard", [
          "bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # 0
    print(countConstruct("enterapotentpot", [
          "a", "p", "ent", "enter", "ot", "o", "t"]))  # 4
    print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                         ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))  # 0


if __name__ == '__main__':
    main()
