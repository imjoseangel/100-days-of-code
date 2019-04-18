#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)

from datetime import date
from typing import Type, TypeVar

TAnimal = TypeVar("TAnimal", bound="Animal")


class Animal:
    def __init__(self, name: str, birthday: date) -> None:
        self.name = name
        self.birthday = birthday

    @classmethod
    def newborn(cls: Type[TAnimal], name: str) -> TAnimal:
        return cls(name, date.today())

    def twin(self: TAnimal, name: str) -> TAnimal:
        cls = self.__class__
        return cls(name, self.birthday)


class Dog(Animal):
    def bark(self) -> None:
        print(f"{self.name} says woof!")


def main():
    fido = Dog.newborn("Fido")
    pluto = fido.twin("Pluto")
    fido.bark()
    pluto.bark()


if __name__ == '__main__':
    main()
