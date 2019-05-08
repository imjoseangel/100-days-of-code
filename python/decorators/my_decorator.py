#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)

from datetime import datetime
import math
import functools
from flask import Flask, request
import decorators

app = Flask(__name__)


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


@decorators.repeat(num_times=4)
def greet2(name):
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


@decorators.slow_down(rate=2)
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)


@decorators.count_calls
def say_whee2():
    print("Whee!")


@decorators.CountCalls
def say_whee3():
    print("Whee!")


@decorators.singleton
class TheOne:
    pass


@decorators.cache
@decorators.count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


@decorators.count_calls
def nocache_fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


@functools.lru_cache(maxsize=4)
def fibonaccifunc(num):
    print(f"Calculating fibonacci({num})")
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


@decorators.set_unit("cm^3")
def volume(radius, height):
    return math.pi * radius**2 * height


@decorators.use_unit("meters per second")
def average_speed(distance, duration):
    return distance / duration


@app.route("/grade", methods=["POST"])
@decorators.validate_json("student_id")
def update_grade():
    json_data = request.get_json()
    # Update database.
    return json_data


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
    greet2("World")
    say_whee2()
    say_whee2()
    print(say_whee2.num_calls)
    counter = decorators.Counter()
    counter()
    counter()
    say_whee3()
    say_whee3()
    print(say_whee3.num_calls)
    first_one = TheOne()
    another_one = TheOne()
    print(id(first_one))
    print(id(another_one))
    print(first_one is another_one)
    nocache_fibonacci(10)
    print(nocache_fibonacci.num_calls)
    print(fibonacci(10))
    print(fibonacci(8))
    fibonaccifunc(10)
    fibonaccifunc(8)
    fibonaccifunc(5)
    fibonaccifunc(8)
    fibonaccifunc(5)
    print(fibonaccifunc.cache_info())
    print(volume(3, 5))
    print(volume.unit)
    bolt = average_speed(100, 9.58)
    print(bolt)
    print(bolt.to("km per hour"))
    print(bolt.to("mph").m)


if __name__ == '__main__':
    main()
