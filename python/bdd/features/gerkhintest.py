#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from gherkin.token_scanner import TokenScanner
from gherkin.token_matcher import TokenMatcher
# from gherkin.pickles.compiler import compile
from gherkin.parser import Parser
# from gherkin.errors import ParserError


def main():

    parser = Parser()

    # gherkin_document = parser.parse("./tutorial.feature")
    # pickles = compile(gherkin_document)
    # print(pickles)

    matcher = TokenMatcher('en')
    feature_file = parser.parse(TokenScanner("./calculator.feature"), matcher)
    print(feature_file['feature']['name'])
    print(feature_file['feature']['children'])


if __name__ == '__main__':
    main()
