#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def circle(r):
    s = pow((math.pi * r), 2)
    return s


def cylinder():

    while True:
        command = int(
            input("Вы что вы хотите посчитать?\n"
                  "Площадь боковой поверхности цилиндра(1)\n"
                  "Или полную площадь цилиндра(2)?\n"
                  ">>> "))
        if (command != 1) & (command != 2):
            print("Неизвестное значение")
            break

        r = int(input("Введите радиус: "))
        h = int(input("Введите высоту: "))

        s = 2 * math.pi * r * h

        if command == 1:
            s = 2 * math.pi * r * h
            print(s)
            break
        elif command == 2:
            s = (2 * math.pi * r * h) + (circle(r) * 2)
            print(s)
            break


if __name__ == '__main__':
    cylinder()
