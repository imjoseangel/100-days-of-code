#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Interactive Dictionary in Python"""

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import os
import json
from difflib import get_close_matches

# Get File Directory
WORK_DIR = os.path.dirname((os.path.realpath(__file__)))

# Loading the json data as python dictionary
DATA = json.load(open(WORK_DIR + "/data/dictionary.json"))


def retrieve_definition(word):
    """Function to Get the Definition of a given word"""
    #Removing the case-sensitivity from the program
    #For example 'Rain' and 'rain' will give same output
    #Converting all letters to lower because out data is in that format
    word = word.lower()
    guessed = len(get_close_matches(word, DATA.keys())) > 0

    #Check for non existing words
    #1st elif: To make sure the program return the definition of
    # words that start with a capital letter (e.g. Delhi, Texas)
    #2nd elif: To make sure the program return the definition of acronyms (e.g. USA, NATO)

    if word in DATA:
        return DATA[word]
    if word.title() in DATA:
        return DATA[word.title()]
    if word.upper() in DATA:
        return DATA[word.upper()]

    #3rd elif: To find a similar word
    #-- len > 0 because we can print only when the word has 1 or more close matches
    #-- In the return statement, the last [0] represents the
    # first element from the list of close matches

    if guessed:
        action = input("Did you mean %s instead? [y or n]: " %
                       get_close_matches(word, DATA.keys())[0])
        #-- If the answers is yes, retrive definition of suggested word
        if action in ('y', 'Y'):
            return DATA[get_close_matches(word, DATA.keys())[0]]
        if action in ('n', 'N'):
            return "The word doesn't exist, yet."

        return "We don't understand your entry. Apologies."

    return None


# Input User
WORD_USER = input("Enter a word: ")

# Retrieve the definition using function and print the result
OUTPUT = retrieve_definition(WORD_USER)

# If a word has more than one definition, print them recursively
if isinstance(OUTPUT, list):
    for item in OUTPUT:
        print("-", item)
# For words with single definition
else:
    print("-", OUTPUT)
