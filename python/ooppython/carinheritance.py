#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=protected-access

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


def charge(device):
    if hasattr(device, '_voltage'):
        print(f"Charging a {device._voltage} volt device")
    else:
        print(f"I can't charge a {device.__class__.__name__}")


class Vehicle:
    def __init__(self, color, model):
        self.color = color
        self.model = model


class Device:
    def __init__(self):
        self._voltage = 12


class Car(Vehicle, Device):
    def __init__(self, color, model, year):
        Vehicle.__init__(self, color, model)
        Device.__init__(self)
        self.year = year

    def __str__(self):
        return f'Car {self.color} : {self.model} : {self.year}'

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, volts):
        print("Warning: this can cause problems!")
        self._voltage = volts

    @voltage.deleter
    def voltage(self):
        print("Warning: the radio will stop working!")
        del self._voltage

    def __eq__(self, other):
        return self.year == other.year

    def __lt__(self, other):
        return self.year < other.year

    def __add__(self, other):
        return Car(self.color + other.color, self.model + other.model,
                   int(self.year) + int(other.year))


class Phone(Device):
    pass


class Rhino:
    pass


def main():

    my_car = Car("yellow", "beetle", 1969)
    print(f"My car is {my_car.color}")
    print(f"My car uses {my_car.voltage} volts")
    my_car.voltage = 6
    print(f"My car now uses {my_car.voltage} volts")
    my_phone = Phone()
    my_rhino = Rhino()
    charge(my_car)
    charge(my_phone)
    charge(my_rhino)

    print(repr(my_car))
    print(str(my_car))

    your_car = Car("red", "Corvette", 1967)
    print(my_car < your_car)
    print(my_car > your_car)
    print(my_car == your_car)
    print(my_car + your_car)

    print(type(my_car))
    print(isinstance(my_car, Car))
    print(isinstance(my_car, Device))

    print(dir(my_car))

    for method_name in dir(my_car):
        if callable(getattr(my_car, method_name)):
            print(method_name)

    for method_name in dir(my_car):
        attr = getattr(my_car, method_name)
        if callable(attr):
            if method_name == '__str__':
                print(attr())


if __name__ == '__main__':
    main()
