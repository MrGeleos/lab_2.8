#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def test():
    num = int(input('Введите число: '))
    if num >= 0:
        positive()
    else:
        negative()


def positive():
    print("Число является положительное")


def negative():
    print("Число является отрицательное")


if __name__ == '__main__':
    test()
