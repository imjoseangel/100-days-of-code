#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=R0914

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)
from pathlib import Path
from enum import Enum, auto
from functools import lru_cache
from dataclasses import dataclass
import time


# Type hinting (3.5+)
def sentence_has_animal(sentence: str) -> bool:
    return "animal" in sentence


# Enumerations (3.4+)
class Monster(Enum):
    ZOMBIE = auto()
    WARRIOR = auto()
    BEAR = auto()


# Built-in LRU cache (3.2+)
def fib(number: int) -> int:
    if number == 0:
        return 0
    if number == 1:
        return 1

    return fib(number - 1) + fib(number - 2)


@lru_cache(maxsize=512)
def fib_memoization(number: int) -> int:
    if number == 0:
        return 0
    if number == 1:
        return 1

    return fib_memoization(number - 1) + fib_memoization(number - 2)


# Extended iterable unpacking (3.0+)
class Armor:
    def __init__(self, armor: float, description: str, level: int = 1):
        self.armor = armor
        self.level = level
        self.description = description

    def power(self) -> float:
        return self.armor * self.level


@dataclass
class Armordataclass:
    armor: float
    description: str
    level: int = 1

    def power(self) -> float:
        return self.armor * self.level


def main():

    # F-Strings (3.6+)
    user = "Jane Doe"
    action = "buy"
    log_message = 'User {} has logged in and did an action {}.'.format(
        user, action)
    print(log_message)
    # User Jane Doe has logged in and did an action buy.

    log_message = f'User {user} has logged in and did an action {action}.'
    print(log_message)
    # User Jane Doe has logged in and did an action buy.

    # Pathlib (3.4+)
    root = Path('post_sub_folder')
    print(root)
    # post_sub_folder
    path = root / 'happy_user'
    # Make the path absolute
    print(path.resolve())
    # /home/weenkus/Workspace/Projects/DataWhatNow-Codes/
    # how_your_python3_should_look_like/post_sub_folder/happy_user

    # Type hinting (3.5+)
    print(sentence_has_animal("Donald had a farm without animals"))
    # True

    # Enumerations (3.4+)
    print(Monster.ZOMBIE)
    # Monster.ZOMBIE

    for monster in Monster:
        print(monster)
    # Monster.ZOMBIE
    # Monster.WARRIOR
    # Monster.BEAR

    # Built-in LRU cache (3.2+)
    start = time.time()
    fib(20)
    print(f'Duration: {time.time() - start}s')
    # Duration: 30.684099674224854s

    start = time.time()
    fib_memoization(20)
    print(f'Duration: {time.time() - start}s')
    # Duration: 6.866455078125e-05s

    # Extended iterable unpacking (3.0+)
    head, *body, tail = range(5)
    print(head, body, tail)
    # 0 [1, 2, 3] 4

    py, filename, *cmds = "python3.7 script.py -n 5 -l 15".split()
    print(py)
    print(filename)
    print(cmds)
    # python3.7
    # script.py
    # ['-n', '5', '-l', '15']

    first, _, third, *_ = range(10)
    print(first, third)
    # 0 2

    # Data classes (3.7+)
    armor = Armor(5.2, "Common armor.", 2)
    armor.power()
    # 10.4
    print(armor)
    # <__main__.Armor object at 0x7fc4800e2cf8>

    armordataclass = Armordataclass(5.2, "Common armor.", 2)
    armordataclass.power()
    # 10.4
    print(armordataclass)
    # Armor(armor=5.2, description='Common armor.', level=2)


if __name__ == '__main__':
    main()
