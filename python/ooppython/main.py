#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import sys
import enemy as en


def main():
    # game start
    foe = en.Enemy("troll", "great axe")
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
