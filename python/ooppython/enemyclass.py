#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import sys
import random


class Enemy():
    def __init__(self, ancestry, gear):
        self.enemy = ancestry
        self.weapon = gear
        self.hp = random.randrange(10, 20)
        self.ac = random.randrange(12, 20)
        self.alive = True

    def fight(self):
        print("You take a swing at the " + self.enemy + ".")
        hit = random.randrange(0, 20)

        if self.alive and hit > self.ac:
            print("You hit the " + self.enemy + " for " + str(hit) +
                  " damage!")
            self.hp = self.hp - hit
            print("The " + self.enemy + " has " + str(self.hp) +
                  " HP remaining")
        else:
            print("You missed.")

        if self.hp < 1:
            self.alive = False


def main():

    # game start
    foe = Enemy("troll", "great axe")
    print("You meet a " + foe.enemy + " wielding a " + foe.weapon)

    # main loop
    while True:

        print("Type the a key and then RETURN to attack.")

        action = input()

        if action.lower() == "a":
            foe.fight()

        if not foe.alive:
            print("You have won...this time.")
            sys.exit()


if __name__ == '__main__':
    main()
