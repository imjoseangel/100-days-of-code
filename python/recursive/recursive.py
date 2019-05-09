#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)

from functools import lru_cache
import sys


# Each function call represents an elf doing his work
def deliver_presents_recursively(houses):
    # Worker elf doing his work
    if len(houses) == 1:
        house = houses[0]
        print("Delivering presents to", house)

    # Manager elf doing his work
    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]

        # Divides his work among two elves
        deliver_presents_recursively(first_half)
        deliver_presents_recursively(second_half)


def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n - 1)


def sum_recursive(current_number, accumulated_sum):
    # Base case
    # Return the final state
    if current_number == 11:
        return accumulated_sum

    # Recursive case
    # Thread the state through the recursive call
    else:
        return sum_recursive(current_number + 1,
                             accumulated_sum + current_number)


# Return a new list that is the result of
# adding element to the head (i.e. front) of input_list
def attach_head(element, input_list):
    return [element] + input_list


@lru_cache(maxsize=None)
def fibonacci_recursive(n):
    print("Calculating F", "(", n, ")", sep="", end=", ")

    # Base case
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def main():
    houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]
    deliver_presents_recursively(houses)

    print(factorial_recursive(5))

    print(sum_recursive(1, 0))

    attach = attach_head(
        1,  # Will return [1, 46, -31, "hello"]
        attach_head(
            46,  # Will return [46, -31, "hello"]
            attach_head(
                -31,  # Will return [-31, "hello"]
                attach_head("hello", []))))  # Will return ["hello"]

    print(attach)

    print(fibonacci_recursive(5))

    print(sys.getrecursionlimit())


if __name__ == '__main__':
    main()
