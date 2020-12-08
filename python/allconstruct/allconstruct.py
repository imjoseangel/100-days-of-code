#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


def allConstruct(target: str, wordBank: list, memo: dict = None) -> list:

    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]

    if target == "":
        return [[]]

    result = []

    for word in wordBank:
        try:
            if target.index(word) == 0:
                suffix = target[len(word):]
                suffixWays = allConstruct(suffix, wordBank)
                targetWays = list(
                    map(lambda way, wrd=word: [*way, wrd], suffixWays))
                result.extend(targetWays)
        except ValueError:
            pass

    memo[target] = result
    return result


def main():
    # [['le', 'purp'], ['le', 'p', 'ur', 'p']]
    print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
    # [['def', 'c', 'ab'], ['ef', 'cd', 'ab'], ['def', 'abc'], ['ef', 'abcd']]
    print(allConstruct("abcdef", ["ab", "abc",
                                  "cd", "def", "abcd", "ef", "c"]))
    print(allConstruct("skateboard", [
          "bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # []
    # [['t', 'o', 'p', 'ent', 't', 'o', 'p', 'a', 'enter'],
    # ['ot', 'p', 'ent', 't', 'o', 'p', 'a', 'enter'],
    # ['ot', 'p', 'ent', 'ot', 'p', 'a', 'enter'],
    # ['t', 'o', 'p', 'ent', 'ot', 'p', 'a', 'enter']]
    print(allConstruct("enterapotentpot", [
          "a", "p", "ent", "enter", "ot", "o", "t"]))
    print(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeez",
                       ["a", "aa", "aaa", "aaaa", "aaaaa"]))  # []


if __name__ == '__main__':
    main()
