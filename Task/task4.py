#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    slova = input("Введите строку: ")
    return slova


def test_input(slova):
    if type(slova) == int:
        return True
    elif slova.isnumeric():
        return True
    else:
        return False


def str_to_int(slova):
    a = int(slova)
    return a


def print_int(slova):
    print(slova)


if __name__ == '__main__':
    stroka = get_input()
    proverka = test_input(stroka)
    if proverka is True:
        print_int(str_to_int(stroka))
    else:
        print("Введённая строка не является числом")
