#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


def allConstruct(target: str, wordBank: list) -> list:
    table = [[]] * (len(target) + 1)
    table[0] = [[]]

    i = 0
    while i <= len(target):
        for word in wordBank:
            if target[i: i + len(word)] == word:
                newCombinations = list(
                    map(lambda subArray, wrd=word: [*subArray, wrd], table[i]))
                table[i + len(word)].extend(newCombinations)
        i += 1

    return table[len(target)]


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
