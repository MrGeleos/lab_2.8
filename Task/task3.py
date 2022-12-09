#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def test():
    print("Введите числа для перемножения. Чтобы закончить, введите 0: ")
    n = 1
    while True:
        s = int(input(">>> "))
        if s == 0:
            break
        else:
            n *= s
    print("Итог перемножения: ", n)


if __name__ == '__main__':
    test()
