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
                suffixWays = allConstruct(suffix, wordBank, memo)
                targetWays = list(
                    map(lambda way, wrd=word: [wrd, *way], suffixWays))
                result.extend(targetWays)
        except ValueError:
            pass

    memo[target] = result
    return result


def main():
    # [['purp', 'le'], ['p', 'ur', 'p', 'le']]
    print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
    # [['ab', 'cd', 'ef'], ['ab', 'c', 'def'], ['abc', 'def'], ['abcd', 'ef']]
    print(allConstruct("abcdef", ["ab", "abc",
                                  "cd", "def", "abcd", "ef", "c"]))
    print(allConstruct("skateboard", [
          "bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # []
    # [['enter', 'a', 'p', 'ot', 'ent', 'p', 'ot'],
    # ['enter', 'a', 'p', 'ot', 'ent', 'p', 'o', 't'],
    # ['enter', 'a', 'p', 'o', 't', 'ent', 'p', 'ot'],
    # ['enter', 'a', 'p', 'o', 't', 'ent', 'p', 'o', 't']]
    print(allConstruct("enterapotentpot", [
          "a", "p", "ent", "enter", "ot", "o", "t"]))
    print(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeez",
                       ["a", "aa", "aaa", "aaaa", "aaaaa"]))  # []


if __name__ == '__main__':
    main()
