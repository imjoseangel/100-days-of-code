#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import random


def enemy(ancestry, gear):
    funcenemy = ancestry
    weapon = gear
    hp = random.randrange(0, 20)
    ac = random.randrange(0, 20)
    return [funcenemy, weapon, hp, ac]


def fight(tgt):
    print("You take a swing at the " + tgt[0] + ".")
    hit = random.randrange(0, 20)
    if hit > tgt[3]:
        print("You hit the " + tgt[0] + " for " + str(hit) + " damage!")
        tgt[2] = tgt[2] - hit
    else:
        print("You missed.")


def main():

    foe = enemy("troll", "great axe")
    print("You meet a " + foe[0] + " wielding a " + foe[1])
    print("Type the a key and then RETURN to attack.")

    while True:
        action = input()

        if action.lower() == "a":
            fight(foe)

        if foe[2] < 1:
            print("You killed your foe!")
        else:
            print("The " + foe[0] + " has " + str(foe[2]) + " HP remaining")


if __name__ == '__main__':
    main()
