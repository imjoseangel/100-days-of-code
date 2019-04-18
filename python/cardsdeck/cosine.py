#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)

import numpy as np  # type: ignore


def print_cosine(x: np.ndarray) -> None:
    with np.printoptions(precision=3, suppress=True):
        print(np.cos(x))


def main():
    x = np.linspace(0, 2 * np.pi, 9)
    print_cosine(x)


if __name__ == '__main__':
    main()
