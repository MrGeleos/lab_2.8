#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def circle(r):
    return math.pi * r ** 2


def cylinder():
    r = float(input("Введите радиус: "))
    h = float(input("Введите высоту: "))
    s = 2 * math.pi * r * h

    command = int(input("Вы что вы хотите посчитать? Площадь боковой поверхности цилиндра(1) или полную площадь цилиндра(2)? "))
    if command == 1:
        print(s)

    elif command == 2:
        print(s + (circle(r) * 2))


if __name__ == '__main__':
    cylinder()
