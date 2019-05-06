#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)


def outer(num1):
    def inner_increment(num1):  # Hidden from outer code
        return num1 + 1

    num2 = inner_increment(num1)
    print(num1, num2)


def factorial(number):

    # Error handling
    if not isinstance(number, int):
        raise TypeError("Sorry. 'number' must be an integer.")
    if not number >= 0:
        raise ValueError("Sorry. 'number' must be zero or positive.")

    def inner_factorial(number):
        if number <= 1:
            return 1
        return number * inner_factorial(number - 1)

    return inner_factorial(number)


def generate_power(number):
    """
    Examples of use:

    >>> raise_two = generate_power(2)
    >>> raise_three = generate_power(3)
    >>> print(raise_two(7))
    128
    >>> print(raise_three(5))
    243
    """

    # Define the inner function ...
    def nth_power(power):
        return number**power

    # ... that is returned by the factory function.

    return nth_power


def generate_power2(exponent):
    def decorator(f):
        def inner(*args):
            result = f(*args)
            return exponent**result

        return inner

    return decorator


@generate_power2(2)
def raise_two(n):
    return n


def main():

    # inner_increment(10)
    outer(10)

    # Call the outer function.
    print(factorial(4))

    raise_three = generate_power(3)
    print(raise_three(4))

    print(raise_two(5))


if __name__ == '__main__':
    main()
