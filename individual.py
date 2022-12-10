#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def get_train(trains):
    destination = input("Пункт назначения? ")
    number = input("Номер поезда? ")
    timer = input("Время отправления (ЧЧ:ММ)? ")

    train = {
        'destination': destination,
        'number': number,
        'timer': timer,
    }
    trains.append(train)
    if len(trains) > 1:
        trains.sort(key=lambda item: item.get('timer', ''))
    return trains


def display_train():
    if trains:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 20
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
                "№",
                "Пункт",
                "Номер поезда",
                "Время отпраления"
            )
        )
        print(line)

        for idx, train in enumerate(trains, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                    idx,
                    train.get('destination', ''),
                    train.get('number', ''),
                    train.get('timer', 0)
                )
            )
        print(line)


def select():

    destination1 = input('Введите название пункта: ')

    count = 0

    for train in trains:
        if train.get('destination', '') == destination1:
            print(
                '{:>1} {}'.format('Пункт: ', train.get('destination', '')),
                '{:>1} {}'.format('Номер поезда: ', train.get('number', '')),
                '{:>1} {}'.format('Время отправления: ', train.get('timer', 0))
            )
            count += 1

    if count == 0:
        print("Поезд с таким пунктом не найден.")


def help_1():
    print("Список комaанд:\n")
    print("add - добавить поезд;")
    print("list - вывести список поезда;")
    print("select - запросить поезд с пунктом назначения;")
    print("exit - завершить работу с программой.")


if __name__ == '__main__':

    trains = []

    while True:

        command = input(">>> ").lower()

        if command == "exit":
            break
        elif command == "add":
            trains = get_train(trains)
        elif command == "list":
            display_train()
        elif command.startswith('select'):
            select()
        elif command == "help":
            help_1()
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
