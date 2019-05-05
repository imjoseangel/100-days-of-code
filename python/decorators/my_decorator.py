#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)

from datetime import datetime
import math
import decorators


def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


@my_decorator
def say_whee():
    print("Whee!")


@decorators.do_twice
def say_whee_from_import():
    print("Whee!")


@decorators.do_twice
def greet(name):
    print(f"Hello {name}")


@decorators.do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


@decorators.timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])


@decorators.debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"


def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))


@decorators.slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)


def main():

    say_whee()
    say_whee_from_import()
    greet("World")
    print(return_greeting("Adam"))
    waste_some_time(1)
    print(make_greeting("Benjamin", age=112))
    math.factorial = decorators.debug(math.factorial)
    approximate_e(5)
    countdown(3)


if __name__ == '__main__':
    main()
