#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)


class Rectangle:
    def __init__(self, length, width, **kwargs):
        self.length = length
        self.width = width
        super().__init__(**kwargs)

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class OldSquare:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length


class Triangle:
    def __init__(self, base, height, **kwargs):
        self.base = base
        self.height = height
        super().__init__(**kwargs)

    def tri_area(self):
        return 0.5 * self.base * self.height


# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length, **kwargs):
        super().__init__(length=length, width=length, **kwargs)
        # same as super(Square, self).__init__(length, length)


class VolumeMixin:
    def volume(self):
        return self.area() * self.height


class Cube(VolumeMixin, Square):
    def __init__(self, length):
        super().__init__(length)
        self.height = length

    def face_area(self):
        return super().area()

    def surface_area(self):
        return super().area() * 6


class OldCube(Square):
    def surface_area(self):
        return super().area() * 6
        # same as super(Square, self).area() * 6

    def volume(self):
        return super().area() * self.length
        # same as super(Square, self).area() * self.length


class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height, **kwargs):
        self.base = base
        self.slant_height = slant_height
        kwargs["height"] = slant_height
        kwargs["length"] = base
        super().__init__(base=base, **kwargs)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

    def area_2(self):
        base_area = super().area()
        triangle_area = super().tri_area()
        return triangle_area * 4 + base_area


def main():
    square = OldSquare(4)
    print(f'Old Square Area: \t{square.area()}')

    square = Square(4)
    print(f'Square Area: \t\t{square.area()}')

    rectangle = Rectangle(2, 4)
    print(f'Rectangle Area: \t{rectangle.area()}')

    cube = Cube(3)
    print(f'Cube Surface Area: \t{cube.surface_area()}')
    print(f'Cube Volume: \t\t{cube.volume()}')

    pyramid = RightPyramid(base=2, slant_height=4)
    print(f'Right Piramid Area: \t{pyramid.area()}')
    print(f'Right Piramid Area 2: \t{pyramid.area_2()}')

    # Print Super Order
    print(RightPyramid.__mro__)


if __name__ == '__main__':
    main()
