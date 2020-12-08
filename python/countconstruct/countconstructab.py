#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


def countConstruct(target: str, wordBank: list) -> int:
    table = [0] * (len(target) + 1)
    table[0] = 1

    i = 0
    while i <= len(target):
        for word in wordBank:
            if target[i: i + len(word)] == word:
                table[i + len(word)] += table[i]
        i += 1

    return table[len(target)]


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
