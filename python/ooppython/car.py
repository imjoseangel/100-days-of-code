#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=protected-access

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


class Car:

    wheels = 0

    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year
        self.__cupholders = 6
        self._voltage = 12

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


def main():

    my_car = Car("yellow", "beetle", 1967)
    print(f"My car is {my_car.color}")

    my_car.wheels = 5
    print(f"Wheels: {my_car.wheels}")

    my_other_car = Car("red", "corvette", "1999")
    print(f"My other car is {my_other_car.color}")

    # Change the class variable value
    Car.wheels = 4
    print(f"My car has {my_car.wheels} wheels")
    print(f"My other car has {my_other_car.wheels} wheels")

    # Paint the car
    my_car.color = "red"

    print(f"It was built in {my_car.year}")
    my_car.year = 1966
    print(f"It was built in {my_car.year}")
    print(f"It has {my_car._Car__cupholders} cupholders")
    # print(f"It has {my_car.__cupholders} cupholders.")

    # Delete year
    del my_car.year
    # print(f"It was built in {my_car.year}")

    # Electric car
    print(f"My car uses {my_car.voltage} volts")

    my_car.voltage = 6
    print(f"My car now uses {my_car.voltage} volts")
    del my_car.voltage


if __name__ == '__main__':
    main()
